#!/bin/bash
set -e

cd covid-api
sam build
sam deploy

#describe API
#aws cloudformation describe-stacks --stack-name basic --region ca-central-1 --query "Stacks[].Outputs"

#aws lambda invoke --function-name covid-app-TriagemFunction-1OIQW0OBHJEO0 --payload '{"paciente": 123456,"temperatura": 36}' /dev/stdout
#aws stepfunctions start-execution --state-machine-arn arn:aws:states:us-east-1:771620814942:stateMachine:CovidStateMachine-aqv8NqziqBbI --input "{\"paciente\":123456, \"temperatura\":38}"

 
 

