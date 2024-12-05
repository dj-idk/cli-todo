"""Logic to handle updating a task"""

from rich.console import Console
from os import path
import json

file_path = path.join(path.dirname(__file__), "tasks.json")
console = Console()


# just take whatever the user wants to insert and update the task if he adds inputs something
def update_task(tasks, selected_task, name="", description=""):
    """updates a task based of what the user has provided."""
    found_task = next((task for task in tasks if task == selected_task), None)
    if found_task:
        if name:
            found_task["name"] = name
        if description:
            found_task["description"] = description
        if description or name:
            console.print(
                f"\nTask '{selected_task.get("name")}' was successfully updated !\n",
                style="bold cyan",
            )
        elif not description and not name:
            console.print("\nTask was not updated!\n", style="bold yellow")

        with open(file_path, "w") as outfile:
            json.dump(tasks, outfile, indent=4)
    else:
        print("Add a Task First!")
