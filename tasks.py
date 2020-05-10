"""
File: tasks.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: Task module.
"""

import datetime
from tasklib import TaskWarrior as TW
from helpers import normalize_task_date


def load_tw_config():
    """
    Load TaskWarrior configuration to get the UDA.
    """
    tw = TaskW()
    return tw.load_config()


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
    today = datetime.datetime.now()
    overdue = list()
    for task in tasks:
        if task['due']:
            if today >= normalize_task_date(task, 'due'):
                overdue.append(task)
    return overdue


def scheduled_tasks(tasks):
    """Filter scheduled tasks.

    :tasks: List of all tasks.
    :returns: List of scheduled tasks.

    """
    today = datetime.datetime.now()
    scheduled = list()
    for task in tasks:
        if task['scheduled']:
            if today >= normalize_task_date(task, 'scheduled'):
                scheduled.append(task)
    return scheduled


def not_date_tasks(tasks):
    """Filter tasks with no due date

    :tasks: List of all tasks.
    :returns: List of scheduled tasks.

    """
    not_due = list()
    for task in tasks:
        if not task['due']:
            # output_task(task)
            not_due.append(task)
    return not_due
