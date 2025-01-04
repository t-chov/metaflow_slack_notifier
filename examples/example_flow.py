import os

from metaflow import FlowSpec, environment, slack, step


class ExampleFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.end)

    @environment(vars={"METAFLOW_SLACK_CHANNEL": "alert"})
    @slack(token=os.getenv("METAFLOW_SLACK_APP_TOKEN"))
    @step
    def end(self):
        1 / 0
        print("end")


if __name__ == "__main__":
    ExampleFlow()
