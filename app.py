#!/usr/bin/env python3

import aws_cdk as cdk

from debug_infrastructure.pipeline_stack import PipelineStack

app = cdk.App()

environments = [
    "DEV"
]

# Create env pipeline stack in tooling account.
for name in environments:
    region = 'ap-southeast-2'
    account = '0000000000'
    project = app.node.try_get_context("project_name")

    stack = PipelineStack(
        app,
        f"{project}-pipeline-{name}",
        env=cdk.Environment(
            account=account,
            region=region,
        ),
        env_name=name,
    )

app.synth()
