# Metaflow Slack Notification Plugin

[![CI](https://github.com/t-chov/metaflow_slack_notifier/actions/workflows/ci.yaml/badge.svg)](https://github.com/t-chov/metaflow_slack_notifier/actions/workflows/ci.yaml)

A Metaflow plugin that sends detailed error notifications to Slack when a flow step fails. This helps teams monitor their Metaflow pipelines and quickly respond to failures.

## Features

- Automatic Slack notifications on step failures
- Detailed error information including:
  - Flow details
  - Retry count and limits
  - Flow parameters
  - Input data
  - Full stack trace
- Easy integration with existing Metaflow pipelines

## Installation

```bash
pip install metaflow-slack-notifier
```

## Configuration

Set the following environment variables:

```bash
export METAFLOW_SLACK_APP_TOKEN="xoxb-your-token"
export METAFLOW_SLACK_CHANNEL="your-channel"
```

or use `@environment` decorator:

```python
@environment(vars={"METAFLOW_SLACK_APP_TOKEN": "xoxb-your-token", "METAFLOW_SLACK_CHANNEL": "your-channel"})
@slack()
@step
def some_step(self):
    # write your code
    print("end")
```

## Usage

Add the `@slack` decorator to any step that you want to monitor.

```python
from metaflow import FlowSpec, slack, step
import os

token = os.getenv("METAFLOW_SLACK_APP_TOKEN")
channel = os.getenv("METAFLOW_SLACK_CHANNEL")

class MyFlow(FlowSpec):
    @step
    def start(self):
        print("start")
        self.next(self.end)

    @slack(token=token, channel=channel)
    @step
    def end(self):
        # This will trigger a Slack notification due to ZeroDivisionError
        1 / 0
        print("end")

if __name__ == "__main__":
    MyFlow()
```

When the step fails, you'll receive a notification in your Slack channel with the error details.

## Slack App Setup

1. Create a new Slack App in your workspace
2. Enable the following OAuth scopes:
    - chat:write
    - chat:write.public (if sending to public channels)
3. Install the app to your workspace
4. Copy the Bot User OAuth Token (starts with xoxb-)

## License

MIT License
