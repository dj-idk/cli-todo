"""Delete's a task from the json file"""

import json
from os import path


file_path = path.join(path.dirname(__file__), "tasks.json")


def delete_task(tasks, selected_task=None):
    """Delete a task from the json file"""
    if selected_task:
        found_task = next((task for task in tasks if task == selected_task), None)
        tasks.remove(found_task)
        with open(file_path, "w") as outfile:
            json.dump(tasks, outfile, indent=4)
        print(f"Task {found_task.get("name")} deleted successfully!")
    else:
        print("Add a Task First!")
