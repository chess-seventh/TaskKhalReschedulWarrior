"""
File: events.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description:  Module for calendar and events for Khal.
"""

import datetime
from datetime import date, timedelta
from logger import logger
from ics import Event
from ics import Calendar


def create_event(task, scheduled):
    """Create an Event based on task parameters.

    :task: Task to create an event from.
    :returns: Event file

    """
    calendar = Calendar()
    event = Event()
    event.name = task['description']
    event.uid = task['uuid']
    event.begin = "1"
    # task and event must have same
    # event.begin = datetime.datetime.now()
    # event.end = datetime.datetime.now()+1


def next_days(day_of_week):
    """Get future days.
    :returns: List of future days.
    """
    today = datetime.datetime.today()
    month = today.month
    year = today.year

    chosen_day = list()
    for sunday in month_chosen_day(year, month, chosen_day):
        chosen_day.append(sunday)
    return chosen_day


def month_chosen_day(year, month, chosen_day):
    """Yields sundays for current month.
    :returns: List of future sundays.

    """
    date_chosen = date(year, month, 1)
    date_chosen += timedelta(days=7 - date_chosen.weekday())
    while date_chosen.year == year and date_chosen.month == month:
        yield date_chosen
        date_chosen += timedelta(days=7)


def event_task_status(task):
    """Check if task on calendar is done.

    :task: Task class to check on calendar.
    :returns: True/False

    """
    # TODO: Check status of Event Task
    logger.debug(task)


def event_task_amend(task, calendar):
    """Amend the calendar task.

    :taks: Task class to change.
    :calendar: Calendar class to configure.
    :returns: New calendar event.

    """
    # TODO: Amend Task Event and Task
    logger.debug(task, calendar)
