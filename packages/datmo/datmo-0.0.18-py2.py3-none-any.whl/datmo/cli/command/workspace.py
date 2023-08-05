from datmo.core.util.i18n import get as __
from datmo.cli.command.project import ProjectCommand
from datmo.core.util.misc_functions import mutually_exclusive
from datmo.cli.driver.helper import Helper
from datmo.core.controller.task import TaskController


class WorkspaceCommand(ProjectCommand):
    def __init__(self, cli_helper):
        super(WorkspaceCommand, self).__init__(cli_helper)

    @Helper.notify_environment_active(TaskController)
    @Helper.notify_no_project_found
    def notebook(self, **kwargs):
        self.cli_helper.echo(__("info", "cli.workspace.notebook"))
        # Creating input dictionaries
        snapshot_dict = {}

        # Environment
        if kwargs.get("environment_id", None) or kwargs.get(
                "environment_paths", None):
            mutually_exclusive_args = ["environment_id", "environment_paths"]
            mutually_exclusive(mutually_exclusive_args, kwargs, snapshot_dict)

        task_dict = {
            "ports": ["8888:8888"],
            "command_list": ["jupyter", "notebook"],
            "mem_limit": kwargs["mem_limit"]
        }

        # Run task and return Task object result
        return self.task_run_helper(task_dict, snapshot_dict,
                                    "cli.workspace.notebook")

    @Helper.notify_environment_active(TaskController)
    @Helper.notify_no_project_found
    def rstudio(self, **kwargs):
        self.cli_helper.echo(__("info", "cli.workspace.rstudio"))
        # Creating input dictionaries
        snapshot_dict = {}

        # Environment
        if kwargs.get("environment_id", None) or kwargs.get(
                "environment_paths", None):
            mutually_exclusive_args = ["environment_id", "environment_paths"]
            mutually_exclusive(mutually_exclusive_args, kwargs, snapshot_dict)

        task_dict = {
            "ports": ["8787:8787"],
            "command_list": [
                "/usr/lib/rstudio-server/bin/rserver", "--server-daemonize=0",
                "--server-app-armor-enabled=0"
            ],
            "mem_limit":
                kwargs["mem_limit"]
        }

        # Run task and return Task object result
        return self.task_run_helper(task_dict, snapshot_dict,
                                    "cli.workspace.rstudio")
