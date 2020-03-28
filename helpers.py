"""
File: helpers.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: Module for function helpers.
"""

def sort_task_urgency(task):
    """Helper to sort tasks by urgency.

    :task: Task class.
    :returns: The tasks' key.

    """
    return task['urgency']
