#!/usr/bin/python

import boto3, json

print("Inicio leitura de mensagem SQS")

sqs = boto3.client('sqs')

q = sqs.get_queue_url(QueueName='DevOps')

response = sqs.receive_message(
    QueueUrl=q["QueueUrl"],
    MaxNumberOfMessages=1,
    VisibilityTimeout=2,
    WaitTimeSeconds=2
)

if 'Messages' in response: 
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    body = json.loads(message['Body'])

    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=q["QueueUrl"],
        ReceiptHandle=receipt_handle
    )

    print(body)
    print(body["idade"])

#for msg in response:
#    msgjson=json.dumps(msg)
#    print(msgjson)
    #print(msgjson["Messages"][0]["Body"])
    #print(response["Messages"][0]["ReceiptHandle"])

    #response = sqs.delete_message(
    #    QueueUrl=q["QueueUrl"],
    #    ReceiptHandle=response["Messages"][0]["ReceiptHandle"]
    #)



#response = sqs.send_message(QueueUrl=q["QueueUrl"], MessageBody=body)

#qtMensagensSolicitadas = 2
#rs = q.get_messages(qtMensagensSolicitadas)

#Quantidade de mensagens que foram realmente lidas
#print len(rs)

#qtMensagens = 0
#while qtMensagens < len(rs):
#	m = rs[qtMensagens]
#	print m.get_body()
#	q.delete_message(m)
#	qtMensagens = qtMensagens + 1

print("Fim da leitura de mensagem SQS")