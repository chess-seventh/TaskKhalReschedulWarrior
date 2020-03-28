"""
File: tasks.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: Task module.
"""

from tasklib import TaskWarrior as TW


def load_tasks(task_config):
    """Load tasks based on parsed config.
    :task_config: TaskWarrior configuration.
    :returns: List of all selected the tasks.

    """
    twar = TW(task_config[0])

    tasks = list()
    taskq = list()
    for task_project in task_config[1]:
        taskq.append(twar.tasks.pending().filter(project=task_project))

    for task_query in taskq:
        for task in task_query:
            tasks.append(task)
    return tasks

def overdue_tasks(tasks):
    """Filter overdue tasks.

    :tasks: List of all tasks.
    :returns: List of all overdue tasks.

    """
    # TODO: Fix filtering of tasks
    overdue = tasks.tasks.filter('+OVERDUE', project='lab')
    if overdue:
        return overdue
    return None


def scheduled_tasks(tasks):
    """Filter scheduled tasks.

    :tasks: List of all tasks.
    :returns: List of scheduled tasks.

    """
    # TODO: Return Scheduled Tasks
    print(tasks)
