"""Module to create a CDK Codepipeline stacks

This creates a pipeline per-environment to deploy application stacks,
plus a self-mutation pipeline for this repository
"""

from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
    aws_s3 as s3,
    aws_iam as iam
)
import aws_cdk as cdk

from debug_infrastructure.pipeline_stage import PipelineStage

class PipelineStack(Stack):
    """Create pipelines to deploy this stack and environment stacks"""

    def __init__(self, scope: Construct, id: str, env_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        project = self.node.try_get_context("project_name")

        input  = pipelines.CodePipelineSource.connection(
            repo_string="reducted/reducted",
            branch="not-exist/reducted",
            connection_arn="arn:aws:codestar-connections:ap-southeast-2:0000000000000:connection/0000000-0000-0000-0000-000000000",
        )

        pipeline_name = f"{project}-pipeline"
        application_pipeline = pipelines.CodePipeline(
            self,
            pipeline_name,
            pipeline_name=f"{project}-{env_name}-pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=input,
                install_commands=[
                    "npm install -g aws-cdk",
                    "pip install -r requirements.txt"
                ],
                commands=[
                    "cdk synth",
                ]
            ),
            publish_assets_in_parallel=False,
            cross_account_keys=True,
            self_mutation=True,
            docker_enabled_for_synth=True,
        )

        application_pipeline.add_stage(
            PipelineStage(
                self,
                f"{env_name}",
                env=cdk.Environment(
                    account=self.node.try_get_context(f"account:{env_name}"),
                    region=self.node.try_get_context(f"region:{env_name}"),
                ),
                env_name=env_name,
            ),
        )
