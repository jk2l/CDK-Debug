from constructs import Construct
import aws_cdk as cdk

from aws_cdk import (
    aws_iam as iam,
    aws_lambda as lambda_
)

from debug_infrastructure.nested.function import LambdaStack

class DebugStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, env_name, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_role = iam.Role(
            scope=self,
            id="LambdaFunctionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                ),
            ],
        )

        LambdaStack(
            self,
            "Nested",
            lambda_role=lambda_role
        )
