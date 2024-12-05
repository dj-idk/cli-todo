"""A function for creating a task."""

import json
from os import path
from rich.console import Console

from task import Task

file_path = path.join(path.dirname(__file__), "tasks.json")
console = Console()


def create_task(name: str, description: str):
    """Creates a task using the given name and description and writes it to task.json"""

    # Implement the logic that reads the file or creates a new array for tasks
    if path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                # If the file exists and is readable, serialize it
                tasks = json.load(file)
            except json.JSONDecodeError:
                # if it's corrupt or not readable, create an empty array
                tasks = []
    else:
        # if the file doesn't exist instantiate an empty array
        tasks = []
    # add the task to array and dump it to the file

    # check to see if there are any tasks that have the same name
    if any(task["name"] == name for task in tasks):
        print(f"Task {name} already exists, aborting task creation.")
        return

    # logic for next id
    if tasks:
        existing_ids = {task["id"] for task in tasks}
        next_id = max(existing_ids) + 1
    else:
        next_id = 1

    if name:
        task = Task(name, description)
        # Create a dictionary for that task object
        task_dictionary = {
            "id": next_id,
            "name": task.name,
            "description": task.description,
            "is_active": task.is_active,
            "status": task.status,
            "date": str(task.date),
        }

        tasks.append(task_dictionary)
        with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)
        console.print(
            f"\nTask '{name}' was successfully created !\n",
            style="bold green",
        )
    else:
        console.print(
            "\nYou must at least provide a name for the task.\n", style="bold yellow"
        )
