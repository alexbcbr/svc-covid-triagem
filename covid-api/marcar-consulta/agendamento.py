import json, boto3
def handler(event, context):

    print('Event:', json.dumps(event))
    token = event.
    print()

    sfn = boto3.client('stepfunctions')

    sfn.send_task_success(taskToken=token, output=result)

    #aws stepfunctions send-task-success --task-token 'AAAAKgAAAAIAAAAAAAAAATnz2PpPKNyzNj+16X9dZETzfUvsYGW65KhBMu9rrm2En+B7IycPg4XrutGExxkcqNunVpAfmwyDZi1YhDYQdf5ziJNMuVJv/M/ZT73l12NN+mXAI3cv0Vmkz4uObZSdK8gsF5a7nJDvN0cCMkg0YsoEIBcleXHdMf2Km+u8kE3vAjvqNU0vt/OOuAzo8JqUnZRBCw/YEj3/546cWoA1VgfWV5MKfLcZoMzd9LHA+/pMGcbndKfAO6pzywDSx4LFKaOkS/2WUkuyEVkFUDktAo23eZi/CUSh0OhdZAi4rHTa8ZBD72hpt+HAsIeblOA+wvtprQKSSSEMKcQTn/3VIXonhLTFQdWewtnSCouaFeREZnfQViTNABHe998O7QOEHU+BtkrkAGrsvcjhd5pUf099E2V1hfLYZmVSvNN9tiYt1bj1hm3VK+vPf9E4udKNC5IQ2LoYWveF5euCkvLa1hF0FIz3TQ1wSg/LsrvYphJMX7N8yndBpes2y+Wvzp3drpMjh6qBiVPhAdHcJFEp1Z1eu2lNnfcQzfaxYw7Mk/9HV3HuiKAVVNmYTSAuDSOTZUybv73Ih1BvIExqOVP+lsMHEogAOgqDIbUtRyHSc2a4NxoTD6QDO6+JUJsv6/Qg6g==\' --task-output '{"status": "confirmed"}'

    '''
    {
    "Records": [
        {
            "messageId": "636bb923-7e66-4dba-b332-fc7ae7c475aa",
            "receiptHandle": "AQEB4eIlv1UaD2T+v3H/SkFkNe4XO51E7E2+VDle7USfAcpbHch819L9EXGcqPSiS2gPxjpl7CGCJ5S+SbmLdnQc2Ji6YhyG5lNdvev+MRs07vSoiZCG2mgjAKOiSkz9KHJiztp2TFvIKnP4Pl3sWivTLnCbFenADAdjKFaxyp/esvqctmENw2wA2vkSCcjBlHwquF+Bohl3c9QenNPyjgLdDZBYJC4mkCBL0ykGwq4lCI8FB/7GaUx0D8rzuJe9YGMCyIaDf8WJemI+k78H2LMuI2E2odNPVARAt0OyCKdgD1HeT1CnAHsFvcfUkjZUwvkf//GP1YzdSjSiV3C431PW/E1Ayf9qQkIAv2tOWP8VxQ7vYqpDv6qyka1KM+RAU1/MFALAG8+8sy9/pk3xsTtmEtAnmNhKRqLEqJjd95hcW08=",
            "body": "{\"MessageTitle\":\"Task started by Step Functions. Waiting for callback with task token.\",\"TaskToken\":\"AAAAKgAAAAIAAAAAAAAAATnz2PpPKNyzNj+16X9dZETzfUvsYGW65KhBMu9rrm2En+B7IycPg4XrutGExxkcqNunVpAfmwyDZi1YhDYQdf5ziJNMuVJv/M/ZT73l12NN+mXAI3cv0Vmkz4uObZSdK8gsF5a7nJDvN0cCMkg0YsoEIBcleXHdMf2Km+u8kE3vAjvqNU0vt/OOuAzo8JqUnZRBCw/YEj3/546cWoA1VgfWV5MKfLcZoMzd9LHA+/pMGcbndKfAO6pzywDSx4LFKaOkS/2WUkuyEVkFUDktAo23eZi/CUSh0OhdZAi4rHTa8ZBD72hpt+HAsIeblOA+wvtprQKSSSEMKcQTn/3VIXonhLTFQdWewtnSCouaFeREZnfQViTNABHe998O7QOEHU+BtkrkAGrsvcjhd5pUf099E2V1hfLYZmVSvNN9tiYt1bj1hm3VK+vPf9E4udKNC5IQ2LoYWveF5euCkvLa1hF0FIz3TQ1wSg/LsrvYphJMX7N8yndBpes2y+Wvzp3drpMjh6qBiVPhAdHcJFEp1Z1eu2lNnfcQzfaxYw7Mk/9HV3HuiKAVVNmYTSAuDSOTZUybv73Ih1BvIExqOVP+lsMHEogAOgqDIbUtRyHSc2a4NxoTD6QDO6+JUJsv6/Qg6g==\"}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1602388270072",
                "SenderId": "AROA3HKBPIBPM3S7KV32D:gSOOWSlLItYQSecPKOZRYemuxKdCToCC",
                "ApproximateFirstReceiveTimestamp": "1602388270077"
            },
            "messageAttributes": {},
            "md5OfBody": "fe392ef67a08fcb452f64e7587db8951",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:771620814942:covid-app-SQSQueueLegacyBooking-19YZOVHH31S5U",
            "awsRegion": "us-east-1"
        }
    ]
}
    '''




    #https://github.com/benkehoe/sfn-callback-urls

#    taskToken = event.TaskToken;


#    SF_NAME = 'CovidStateMachine-zdrFndEJZYC9'

#    HELLO_WORLD_SF_DEF = '{"StartAt": "HelloWorld", "States": ' \
#                     '{"HelloWorld": {"Type": "Pass", "Result": "Hello World!", "End": true}}}'

    #ROLE_ARN = 'roleArn'

#    sfn.sendTaskSuccess(
#        name=SF_NAME,
#        definition=HELLO_WORLD_SF_DEF
#    )

    return { 
        'consulta' : 'agendada'
    }
