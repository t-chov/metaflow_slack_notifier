from metaflow import FlowSpec
from metaflow.decorators import StepDecorator


class SlackDecorator(StepDecorator):
    name = "slack"

    def task_finished(
            self,
            step_name: str,
            flow: FlowSpec,
            graph,
            is_task_ok: bool,
            retry_count,
            max_user_code_retries
    ) -> None:
        """
        Run after the task context has been finalized.

        is_task_ok is set to False if the user code raised an exception that
        was not handled by any decorator.

        Note that you can't create or modify data artifacts in this method
        since the task has been finalized by the time this method
        is called. Also note that the task may fail after this method has been
        called, so this method may get called multiple times for a task over
        multiple attempts, similar to all task_ methods.
        """
        print("FOO")
        print(flow)
        print([param for param in flow._get_parameters()])
        print(flow.input)
        print(flow.foreach_stack())
        pass


STEP_DECORATORS_DESC = [("slack", ".SlackDecorator")]
