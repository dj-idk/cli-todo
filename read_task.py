"""Handles the logic for reading task for or reading a task"""

import inquirer
from os import path
import json

import inquirer.themes

file_path = path.join(path.dirname(__file__) + "/tasks.json")


def read_all_tasks():
    """Read all tasks from the taks.json file, allows you to select a certain task and returns it's name"""
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
            choices=[task["name"] for task in tasks],
            carousel=True,
            default=tasks[0],
        )
    ]
    answer = inquirer.prompt(options, theme=inquirer.themes.BlueComposure())
    return answer.get("select-todo")


print(read_all_tasks())
