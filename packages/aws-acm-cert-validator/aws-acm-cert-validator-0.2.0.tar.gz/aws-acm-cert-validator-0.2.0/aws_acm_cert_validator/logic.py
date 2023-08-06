import logging
import time
import boto3

log = logging.getLogger()
log.setLevel(logging.INFO)


class AwsAcmCertValidatorLogic:
    def request(self, domain_name):
        log.info(f"Requesting SSL certificate {domain_name}")
        
        # request certificate
        acm = boto3.client('acm')
        acm_response = acm.request_certificate(DomainName=domain_name, ValidationMethod='DNS')
        cert_arn = acm_response['CertificateArn']
        log.info(f"Certificate to be validated using DNS: {cert_arn}")
        return cert_arn
    
    def validate(self, cert_arn):
        """
        Supports DNS validation only
        :param cert_arn:
        :return:
        """
        log.info(f"Validating cert {cert_arn}")
        acm = boto3.client('acm')
        cert_info = acm.describe_certificate(CertificateArn=cert_arn)
        validation_options = cert_info['Certificate']['DomainValidationOptions'][0]
        while 'ResourceRecord' not in validation_options:
            log.info("Waiting for validation options DNS record in response")
            time.sleep(5)
            cert_info = acm.describe_certificate(CertificateArn=cert_arn)
            validation_options = cert_info['Certificate']['DomainValidationOptions'][0]
        
        dns_validation_record = validation_options['ResourceRecord']
        validated_domain = validation_options['DomainName']
        validated_domain_zone = validated_domain[validated_domain.index('.') + 1:]
        self._create_route53_record(dns_validation_record,
                                    validated_domain,
                                    validated_domain_zone)
        return dns_validation_record
    
    def remove_validation_record(self, domain, dns_record):
        dns_zone = domain[domain.index('.') + 1:]
        route53 = boto3.client('route53')
        hosted_zone = route53.list_hosted_zones_by_name(
            DNSName=dns_zone
        )
        if len(hosted_zone['HostedZones']) == 0:
            raise Exception(f"Zone {dns_zone} is not managed via Route53 in this AWS Account")
        hosted_zone_id = hosted_zone['HostedZones'][0]['Id']
        
        update_request = {
            'Comment': f"Remove certification validation for {domain}",
            'Changes': [
                {
                    'Action': 'DELETE',
                    'ResourceRecordSet': {
                        'Name': dns_record['Name'],
                        'Type': dns_record['Type'],
                        'TTL': 60,
                        'ResourceRecords': [{
                            'Value': dns_record['Value']
                        }],
                    }
                },
            ]
        }
        print(update_request)
        route53.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch=update_request
        )
    
    def _create_route53_record(self, dns_record, validated_domain, dns_zone):
        route53 = boto3.client('route53')
        hosted_zone = route53.list_hosted_zones_by_name(
            DNSName=dns_zone
        )
        if len(hosted_zone['HostedZones']) == 0:
            raise Exception(f"Zone {dns_zone} is not managed via Route53 in this AWS Account")
        hosted_zone_id = hosted_zone['HostedZones'][0]['Id']
        
        update_request = {
            'Comment': f"Certification validation for {validated_domain}",
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': dns_record['Name'],
                        'Type': dns_record['Type'],
                        'TTL': 60,
                        'ResourceRecords': [{
                            'Value': dns_record['Value']
                        }],
                    }
                },
            ]
        }
        print(update_request)
        route53.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch=update_request
        )
    
    def wait_cert_validated(self, cert_arn, max_wait_secs=240, wait_interval_secs=10 , return_empty_on_timeout=False):
        """
        Wait for certificate validation status to move in
         'SUCCESS' state
        :param cert_arn:
        :return:
        """
        log.info(f"Waiting for validation success of {cert_arn}")
        acm = boto3.client('acm')
        validation_status = None
        start = time.time()
        while validation_status is None or validation_status != 'SUCCESS':
            cert_info = acm.describe_certificate(CertificateArn=cert_arn)['Certificate']
            validation_options = cert_info['DomainValidationOptions'][0]
            validation_status = validation_options['ValidationStatus']
            if validation_status != 'SUCCESS':
                wait_secs = time.time() - start
                log.info(f"Max wait: {max_wait_secs}. Current wait: {wait_secs}")
                if wait_secs >= max_wait_secs:
                    if return_empty_on_timeout:
                        return None
                    raise Exception(
                        f"Timeout Error: Certificate for {cert_info['Subject']} did not validate in {max_wait_secs} seconds")
                sleep_time = wait_interval_secs
                if wait_interval_secs + wait_secs > max_wait_secs:
                    sleep_time = max_wait_secs - wait_secs

                log.info(
                    f"Certificate for {cert_info['Subject']} not validated yet, waiting {sleep_time} sec..")
                time.sleep(sleep_time)
        
        # if code path made it this trough cert is validated
        log.info(f"Certificate for {cert_info['Subject']} has been successfully validated")
        return cert_arn
