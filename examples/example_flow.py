import os

from metaflow import FlowSpec, slack, step

token = os.getenv("SLACK_APP_TOKEN")
channel = os.getenv("SLACK_CHANNEL")


class ExampleFlow(FlowSpec):
    @step
    def start(self):
        print("start")
        self.next(self.end)

    @slack(token=token, channel=channel)
    @step
    def end(self):
        1 / 0
        print("end")


if __name__ == "__main__":
    ExampleFlow()
