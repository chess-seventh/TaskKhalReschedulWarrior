"""
File: helpers.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: Module for function helpers.
"""

import datetime
from logger import logger


def sort_task_urgency(task):
    """Helper to sort tasks by urgency.

    :task: Task class.
    :returns: The tasks' urgency.

    """
    return task['urgency']


def sort_task_scheduled(task):
    """Helper to sort tasks by scheduled date.

    :task: Task class.
    :returns: The tasks' scheduled date.

    """
    return task['scheduled']


def sort_task_due(task):
    """Helper to sort tasks by due date.

    :task: Task class.
    :returns: The tasks' due date.

    """
    return task['due']


def normalize_task_date(date, key):
    """Due/Scheduled dates in TaskWarrior contain the TimeZone. This function
    normalizes this so we can work properly.

    :date: The date to normalize.
    :returns: TODO

    """
    if isinstance(date[key], datetime.datetime):
        return date[key].replace(tzinfo=None)
    return None

def output_task(task):
    """TODO: Docstring for output_task.

    :task: The task to output.
    :returns: None

    """
    logger.debug('%s' % [task['uuid'], task['due'], task])
