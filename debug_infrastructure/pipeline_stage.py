import aws_cdk as cdk
from constructs import Construct

from debug_infrastructure.debug_stack import DebugStack


class PipelineStage(cdk.Stage):
    def __init__(self, scope: Construct, id: str, env_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.debug = DebugStack(
            self,
            "debug",
            env=cdk.Environment(
                account=self.node.try_get_context(f"account:{env_name}"),
                region=self.node.try_get_context(f"region:{env_name}"),
            ),
            env_name=env_name,
            termination_protection=True,
        )
