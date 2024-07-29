import aws_encryption_sdk
import boto3
from aws_encryption_sdk import CommitmentPolicy
import json




def lambda_handler(event, context):
  print(json.dumps(event))
  print("Hello World")