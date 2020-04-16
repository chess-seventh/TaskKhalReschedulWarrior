"""
File: helpers.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: Module for function helpers.
"""

import datetime
# from subprocess import PIPE, run
import subprocess
import pytz
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


def set_task_date(task_date):
    """Sets the task date to proper formatting.
    :task_date: The tasks date.
    :return: The changed date for task.

    """
    return pytz.timezone('Europe/Zurich').localize(task_date)


def execute(khal_calendar, calendar_file):
    """Execute Khal import command in shell.

    :calendar_file: Calendar file to import in Khal.
    :returns: The exit result of the command.
    """
    command = ["khal", "import", "-a"] + khal_calendar
    command.append(calendar_file)
    command.append("--batch")  # no confirmations

    subprocess.check_output(command)

    # return result
