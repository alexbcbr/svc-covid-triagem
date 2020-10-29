#!/usr/local/bin/python3

import boto3,json

sfn = boto3.client('stepfunctions')
sqs = boto3.client('sqs')

print("*** INICIO DE EXPEDIENTE ***")

queue="covid-app-SQSQueueLegacyBooking-WE5H3IEX83JQ"

q = sqs.get_queue_url(QueueName=queue)

response = sqs.receive_message(
    QueueUrl=q["QueueUrl"],
    MaxNumberOfMessages=1,
    VisibilityTimeout=2,
    WaitTimeSeconds=2
)

if 'Messages' in response: 
    print("*** AGENDANDO PACIENTE ***:")
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    body = json.loads(message['Body'])

    token = str(body["TaskToken"])
    print(token)

    response = sfn.send_task_success(
        taskToken=token,
        output='{}'
    )

    sqs.delete_message(
        QueueUrl=q["QueueUrl"],
        ReceiptHandle=receipt_handle
    )

print("*** FIM DE EXPEDIENTE ***")
