"""Main menu for cli todo list application."""

# Import 3rd party libraries
import inquirer
from inquirer import themes

from create_task import create_task

# Ask the user for input and see what kind of operation he wants to perform.

questions = [
    inquirer.List(
        name="todo",
        message="Please select an operation",
        choices=[
            "Create a Task",
            "Read a Task",
            "Update a Task",
            "Delete a Task",
            "Exit",
        ],
        carousel=True,
        default="Create a Task",
    )
]


while True:

    answer = inquirer.prompt(questions, theme=themes.BlueComposure())

    if answer.get("todo") == "Create a Task":
        creation_questions = [
            inquirer.Text("name", message="Enter the task name"),
            inquirer.Text("description", message="Enter the task description"),
        ]
        creation_answer = inquirer.prompt(creation_questions)
        task_name = creation_answer.get("name")
        task_description = creation_answer.get("description")
        create_task(task_name, task_description)
        print(f"\nTask '{task_name}' was successfully created !\n")

    elif answer.get("todo") == "Read a Task":
        print("Reading a task")
    elif answer.get("todo") == "Delete a Task":
        print("Deleting a task")
    elif answer.get("todo") == "Update a Task":
        print("Updating a task")
    elif answer.get("todo") == "Exit":
        print("Goodbye!")
        break
