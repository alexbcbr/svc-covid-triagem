import json, boto3
def handler(event, context):

    print('Event:', json.dumps(event))
    print('Context:', context)
    sfn = boto3.client('stepfunctions')

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
