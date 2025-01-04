import os
import traceback

from metaflow import FlowSpec
from metaflow.decorators import StepDecorator
from metaflow.graph import FlowGraph

from .slack import send_message


class SlackDecorator(StepDecorator):
    name = "slack"
    defaults = {
        "token": None,  # Slack API token for authentication
        "channel": None,  # Target Slack channel for notifications
    }

    def task_exception(
        self,
        exception: Exception,
        step_name: str,
        flow: FlowSpec,
        graph: FlowGraph,
        retry_count: int,
        max_user_code_retries: int,
    ) -> None:
        """Handles exceptions by sending error information to Slack."""
        message = f"```\n{str(flow)}\n"
        message += f"retry_count           : {retry_count}\n"
        message += f"max_user_code_retries : {max_user_code_retries}\n"
        message += f"params                : {[param for param in flow._get_parameters()]}\n"
        message += f"input                 : {flow.input}\n"
        message += f"foreach               : {flow.foreach_stack()}\n"
        message += f"{traceback.format_exc()}```"

        token = self.attributes["token"]
        if token is None:
            token = os.getenv("METAFLOW_SLACK_APP_TOKEN")

        channel = self.attributes["channel"]
        if channel is None:
            channel = os.getenv("METAFLOW_SLACK_CHANNEL")

        send_message(token=token, channel=channel, message=message)


STEP_DECORATORS_DESC = [("slack", ".SlackDecorator")]
