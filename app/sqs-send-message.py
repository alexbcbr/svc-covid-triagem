#!/usr/bin/python

import boto3, json

print("Inicio Envio de mensagem SQS")

sqs = boto3.client('sqs')

body=json.dumps({'nome': 'ALEX' , 'idade': '10'})

q = sqs.create_queue(QueueName='DevOps')
response = sqs.send_message(QueueUrl=q["QueueUrl"], MessageBody=body)
print(response)


print("Fim de envio de mensagem SQS")