from metaflow import FlowSpec, step
from metaflow import slack


class ExampleFlow(FlowSpec):
    @slack
    @step
    def start(self):
        print("start")
        self.next(self.end)

    @step
    def end(self):
        print("end")


if __name__ == "__main__":
    ExampleFlow()
