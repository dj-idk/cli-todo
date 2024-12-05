from datetime import datetime


class Task:
    """A model for task"""

    def __init__(
        self,
        name=str,
        description=None or str,
    ):
        """Intializes the primary attributes of the task object"""
        self.name = name
        self.description = description
        self.is_active = True
        self.status = "Pending"
        self.date = datetime.now()

    def __str__(self):
        """Returns a string representation of the task"""
        return self.name
