"""Main menu for cli todo list application."""

# Import 3rd party libraries
import inquirer
import pyfiglet
from inquirer import themes
from rich.console import Console
from rich.table import Table

from datetime import datetime

from create_task import create_task
from read_task import get_tasks, select_task
from update_task import update_task
from delete_task import delete_task

if __name__ == "__main__":

    console = Console()

    while True:
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

        answer = inquirer.prompt(questions, theme=themes.BlueComposure())

        # Create a task
        try:
            if answer.get("todo") == "Create a Task":
                creation_questions = [
                    inquirer.Text("name", message="Enter the task name"),
                    inquirer.Text("description", message="Enter the task description"),
                ]
                creation_answer = inquirer.prompt(creation_questions)
                task_name = creation_answer.get("name")
                task_description = creation_answer.get("description")
                create_task(task_name, task_description)

            # Read all tasks
            elif answer.get("todo") == "Read a Task":
                tasks = get_tasks()
                table = Table()
                table.add_column("ID", style="bright_blue", no_wrap=True)
                table.add_column("Name", style="bold bright_green")
                table.add_column("Description", style="italic yellow")
                table.add_column("Date Added", style="bright_cyan")
                for task in tasks:
                    table.add_row(
                        str(task["id"]),
                        task["name"].title(),
                        task["description"],
                        datetime.fromisoformat(f"{task["date"]}").strftime(
                            "%B %d, %Y at %I:%M:%S %p"
                        ),
                    )
                print("\n")
                console.print(table, style="blink")
                print("\n")
                selected_task = select_task(tasks, " to Read")
                # Read a task
                if selected_task:
                    table = Table()
                    table.add_column("ID", style="bright_blue", no_wrap=True)
                    table.add_column("Name", style="bold bright_green")
                    table.add_column("Description", style="italic yellow")
                    table.add_column("Date Added", style="bright_cyan")
                    table.add_row(
                        str(selected_task["id"]),
                        selected_task["name"].title(),
                        selected_task["description"],
                        datetime.fromisoformat(f"{selected_task["date"]}").strftime(
                            "%B %d, %Y at %I:%M:%S %p"
                        ),
                    )
                    print("\n")
                    text = pyfiglet.figlet_format(
                        f"Task : {selected_task["name"].title()}", font="slant"
                    )
                    console.print(
                        f"[bold green]{text}[/bold green]",
                        width=1000,
                        justify="full",
                    )
                    console.print(table, style="blink", justify="full")
                    print("\n")
                else:
                    console.print(
                        "\nNo task selected or available.\n", style="bold red"
                    )

            # Update a task
            elif answer.get("todo") == "Update a Task":
                tasks = get_tasks()
                if tasks:
                    selected_task = select_task(tasks, " to Update")
                    update_questions = [
                        inquirer.Text(
                            "name",
                            message="Update the task name",
                            default=selected_task.get("name"),
                        ),
                        inquirer.Text(
                            "description",
                            message="Update the task description",
                            default=selected_task.get("description"),
                        ),
                    ]
                    update_answer = inquirer.prompt(update_questions)
                    task_name = update_answer.get("name")
                    task_description = update_answer.get("description")
                    update_task(tasks, selected_task, task_name, task_description)
                else:
                    console.print(
                        "\nNo Tasks Available. Please Create a Task First.\n",
                        style="bold yellow",
                    )

            # Delete a task
            elif answer.get("todo") == "Delete a Task":
                tasks = get_tasks()
                if tasks:
                    selected_task = select_task(tasks, " to Delete")
                    delete_questions = [
                        inquirer.Confirm(
                            "continue",
                            message="Are you sure if you want to delete this task ?",
                        )
                    ]
                    deletion_answer = inquirer.prompt(delete_questions)
                    if deletion_answer.get("continue"):
                        delete_task(tasks, selected_task)
                        console.print(
                            f"\nTask '{selected_task.get("name")}' was successfully deleted !\n",
                            style="bold green",
                        )
                    else:
                        console.print("\n Deletion Aborted", style="bold yellow")
                        continue
                else:
                    console.print(
                        "\nNo Tasks Available. Please Create a Task First.\n",
                        style="bold yellow",
                    )

            # Exit the loop
            elif answer.get("todo") == "Exit":
                console.print(
                    pyfiglet.figlet_format("GOOD BYE !", font="slant"),
                    style="bold purple",
                )
                break
        except AttributeError:
            console.print("\n App closed unexpectedly !", style="bold red")
            break
