import inquirer
from inquirer import themes

import json
from os import path
from datetime import datetime


file_path = path.join(path.dirname(__file__), "tasks.json")


def get_tasks():
    """Retrieves all tasks from the file."""
    if path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                tasks = json.load(file)

            except json.JSONDecodeError:
                return []
    else:
        return []

    tasks.sort(key=lambda task: task["date"], reverse=True)
    return tasks


def select_task(tasks, message=""):
    """Prompts the user to select a task using inquirer."""
    if not tasks:
        return None

    read_options = [
        inquirer.List(
            name="select-todo",
            message="Please select a task" + message,
            choices=[f"{task['id']} - {task['name']}" for task in tasks],
            carousel=True,
        )
    ]
    read_answer = inquirer.prompt(read_options, theme=themes.BlueComposure())
    selected_id = int(read_answer.get("select-todo").split(" - ")[0])
    selected_task = next((task for task in tasks if task["id"] == selected_id), None)
    return selected_task
