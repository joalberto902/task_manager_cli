import argparse
import task_cli.task_manager as task_manager
import os
import json
from typing import Any

TASK_ARCHIVE = "task_objects.json"
def load_tasks(file_path: str) -> dict[str, dict[str, Any]]:
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            task_str: str = f.read()
            task_dict = json.loads(task_str)
            return task_dict
    return {}

def write_tasks(file_path:str, output_dict: dict) -> None:
    task_str: str = json.dumps(output_dict)
    with open(file_path , "w") as f:
        f.write(task_str)

def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="task-cli",
        description="A task manager interface for the command line",
        epilog="Example: task-cli add 'make this work'"
    )

    subparsers = parser.add_subparsers(
        title="Commands",
        dest="command",
        required=True,
    )

    add_command = subparsers.add_parser(
        "add",
        help="Add a new task to the list of task"
    )
    add_command.add_argument("description", 
                             help="The description of the task to be add",
                             type=str)

    update_command = subparsers.add_parser(
        "update",
        help="Given the id and a new description, change the old description to new"
    )
    update_command.add_argument("id", 
                                help="The unique id of the task",
                                type = int)
    update_command.add_argument("description", 
                                help="The new description of the task", 
                                type = str)
  
    delete_command = subparsers.add_parser(
        "delete",
        help="Deletes a task given its id",
    )
    delete_command.add_argument("id",
                                help="The id of the task to be deleted",
                                type = int)

    mark_in_progress_command = subparsers.add_parser(
        "mark-in-progress",
        help="Marks the task as in-progress given its id"
    )
    mark_in_progress_command.add_argument("id", 
                                          help="The id of the task to be marked in-progress",
                                          type = int)

    mark_done_command = subparsers.add_parser(
        "mark-done",
        help="Marks the task as done given its id"
    )
    mark_done_command.add_argument("id", 
                                   help="The id of the task to be marked done", 
                                   type= int)

    list_command = subparsers.add_parser(
        "list",
        help="Lists all of the tasks of a given status, if no status is given, all tasks are listed by default"
    )
    list_command.add_argument(
        "status", 
        default="all", 
        nargs="?",
        choices=["done", "in-progress", "todo", "all"],
        help="The status to be listed")

    args: argparse.Namespace = parser.parse_args()
    task_dict: dict = load_tasks(TASK_ARCHIVE)
    try:
        match args.command:
            case "add":
                output_dict = task_manager.add(args.description, task_dict)
            case "update":
                output_dict = task_manager.update(args.id, args.description, task_dict)
            case "delete":
                output_dict = task_manager.delete(args.id, task_dict)
            case "mark-in-progress":
                output_dict = task_manager.mark_in_progress(args.id, task_dict)
            case "mark-done":
                output_dict = task_manager.mark_done(args.id, task_dict)
            case "list":
                output_dict = task_manager.list_tasks(args.status, task_dict)
    except Exception as e:
        print(f"ERROR: {e}")
        return 1

    write_tasks(TASK_ARCHIVE, output_dict)

    return 0

if __name__ == "__main__":
    main()
