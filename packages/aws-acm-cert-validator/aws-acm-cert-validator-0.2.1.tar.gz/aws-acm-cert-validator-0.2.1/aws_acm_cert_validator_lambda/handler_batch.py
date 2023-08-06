import time

import boto3
import json
import os
import sys
import traceback

MAX_WAIT_TIME = int(os.environ.get('MAX_WAIT_TIME', '600'))

sys.path.append(f"{os.environ['LAMBDA_TASK_ROOT']}/lib")
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import cr_response


def lambda_handler(event, context):
    try:
        if request_type == 'Create':
            # create and validate cert
            issue_validate_cert_respond(domain_name, event, context)
            return

            # physical id should depend on domain name

        if request_type == 'Update' or request_type == 'Delete':
            r = cr_response.CustomResourceResponse(event)
            r.respond({})
            return
    except Exception as ex:
        print("Failed CCR Provisioning. Payload:\n" + str(event))
        print(str(ex))
        traceback.print_exc(file=sys.stdout)
        # if there is fallback ARN provided, respond with fallback arn
        if 'FallbackCertificateArn' in event['ResourceProperties']:
            r = cr_response.CustomResourceResponse(event)
            event['PhysicalResourceId'] = event['ResourceProperties']['FallbackCertificateArn']
            r.respond({'CertificateArn': event['ResourceProperties']['FallbackCertificateArn']})
        else:
            r = cr_response.CustomResourceResponse(event)
            r.respond_error(str(ex))

        return


def issue_validate_cert_respond(domain_name, event, context):
    logic = AwsAcmCertValidatorLogic()

    if 'WaitOnly' in event and event['WaitOnly']:
        acm_certificate_arn = event['PhysicalResourceId']
        validation_record = event['ValidationRecord']
    else:
        acm_certificate_arn = logic.request(domain_name=domain_name)
        validation_record = logic.validate(cert_arn=acm_certificate_arn)

    remaining_lambda_time = (context.get_remaining_time_in_millis() / 1000) - 20
    print(f"Remaining wait secs:{remaining_lambda_time}")
    if 'StartWait' not in event:
        start_wait = time.time()
    else:
        start_wait = int(event['StartWait'])

    result = logic.wait_cert_validated(
        cert_arn=acm_certificate_arn,
        wait_interval_secs=5,
        max_wait_secs=remaining_lambda_time,
        return_empty_on_timeout=True
    )
    if result is None:
        lambda_client = boto3.client('lambda')
        function_name = os.environ['AWS_LAMBDA_FUNCTION_NAME']
        event['PhysicalResourceId'] = acm_certificate_arn
        event['WaitOnly'] = True
        event['ValidationRecord'] = validation_record
        if 'StartWait' not in event:
            event['StartWait'] = start_wait
        if 'WaitIteration' not in event:
            event['WaitIteration'] = 2
        else:
            event['WaitIteration'] += 1

        # if total wait time elapsed raise exception
        if int(time.time()) - int(event['StartWait']) > MAX_WAIT_TIME:
            raise Exception(f"Total wait time of {MAX_WAIT_TIME} elapsed")

        lambda_client.invoke(
            FunctionName=function_name,
            Payload=json.dumps(event).encode('utf-8'),
            InvocationType='Event'
        )
        return

    # remove dns record
    logic.remove_validation_record(domain_name, validation_record)
    # respond
    r = cr_response.CustomResourceResponse(event)
    event['PhysicalResourceId'] = acm_certificate_arn
    r.respond({'CertificateArn': acm_certificate_arn})
