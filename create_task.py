"""A function for creating a task."""

from task import Task
import json
from os import path


def create_task(name: str, description: str):
    """Creates a task using the given name and description and writes it to task.json"""
    # Create a instance of the task class
    task = Task(name, description)
    # Create a dictionary for that task object
    task_dictionary = {
        "name": task.name,
        "description": task.description,
        "is_active": task.is_active,
        "status": task.status,
        "date": str(task.date),
    }
    # Create a variable for the file path
    file_path = path.join(path.dirname(__file__), "tasks.json")

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
    tasks.append(task_dictionary)
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)


create_task("Write python cli todo app", "Make it work before the end of the day")
create_task("Write python cli todo again", "Make it work before the end of the day")
