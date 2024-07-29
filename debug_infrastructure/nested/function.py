from datetime import datetime, timezone

from aws_cdk import (
    aws_lambda as lambda_
)

import aws_cdk as cdk
from constructs import Construct

class LambdaStack(cdk.NestedStack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        lambda_role,
        **kwargs,
    ):
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_function = lambda_.Function(
            self,
            "DebugCdk",
            runtime=lambda_.Runtime.PYTHON_3_12,
            function_name="debug-cdk-nested",
            description="DebugCDK asset bundling fail",
            code=lambda_.Code.from_asset(
                "./lambda/debug/demo",
                bundling=cdk.BundlingOptions(
                    image=lambda_.Runtime.PYTHON_3_12.bundling_image,
                    command=[
                        "bash",
                        "-c",
                        " && ".join(
                            [
                                f"pip install -r requirements.txt -t /{cdk.AssetStaging.BUNDLING_OUTPUT_DIR}",
                                f"cp -r . /{cdk.AssetStaging.BUNDLING_OUTPUT_DIR}",
                                f"echo {datetime.now(timezone.utc)} > /{cdk.AssetStaging.BUNDLING_OUTPUT_DIR}/timestamp"
                            ]
                        ),
                    ],
                ),
            ),
            handler="lambda.lambda_handler",
            role=lambda_role,
            timeout=cdk.Duration.seconds(300),
        )