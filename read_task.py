"""Handles the logic for reading task for or reading a task"""

import inquirer
from os import path
import json

import inquirer.themes

file_path = path.join(path.dirname(__file__) + "/tasks.json")


def read_task():
    """Uses inquirer to select a task and returns the selected task"""
    if path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

    options = [
        inquirer.List(
            name="select-todo",
            message="Please select a task",
            choices=[f"{task["id"]} - {task["name"]}" for task in tasks],
            carousel=True,
            default=tasks[0],
        )
    ]
    answer = inquirer.prompt(options, theme=inquirer.themes.BlueComposure())
    selected_id = int(answer.get("select-todo").split(" - ")[0])
    selected_task = next((task for task in tasks if task["id"] == selected_id), None)
    return selected_task
