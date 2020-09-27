import boto3

# The Amazon Resource Name (ARN) of the state machine to execute.
# Example - arn:aws:states:us-west-2:112233445566:stateMachine:HelloWorld-StateMachine
STATE_MACHINE_ARN = 'arn:aws:states:us-east-1:771620814942:stateMachine:detectar-covid19'

#The name of the execution
EXECUTION_NAME = 'sdk-python'

#The string that contains the JSON input data for the execution
INPUT = '{"paciente":123456, "temperatura":38}'

sfn = boto3.client('stepfunctions')

response = sfn.start_execution(
    stateMachineArn=STATE_MACHINE_ARN,
    name=EXECUTION_NAME,
    input=INPUT
)

#display the arn that identifies the execution
print(response.get('executionArn'))


