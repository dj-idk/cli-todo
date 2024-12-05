"""Main menu for cli todo list application."""

# Import 3rd party libraries
import inquirer
from inquirer import themes
from rich.console import Console
from rich.table import Table
from rich.text import Text

from create_task import create_task
from read_task import read_task

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
console = Console()

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
        result = read_task()

        table = Table()
        table.add_column("ID", style="bright_blue", no_wrap=True)
        table.add_column("Name", style="bold bright_green")
        table.add_column("Description", style="italic yellow")
        table.add_column("Date Added", style="bright_cyan")
        table.add_row(
            str(result.get(("id"))),
            result.get("name").title(),
            result.get("description"),
            result.get("date"),
        )
        console = Console()
        print("\n")
        console.print(table, style="blink")
        print("\n")

    elif answer.get("todo") == "Delete a Task":
        print("Deleting a task")
    elif answer.get("todo") == "Update a Task":
        print("Updating a task")
    elif answer.get("todo") == "Exit":
        console.print("Goodbye!\n", style="bold green")
        break
