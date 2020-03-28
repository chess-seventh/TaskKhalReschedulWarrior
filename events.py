"""
File: events.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description:  Module for calendar and events for Khal.
"""

import datetime
from datetime import date, timedelta
from ics import Event
# from ics import Calendar


def create_event(task):
    """Create an Event based on task parameters.

    :task: Task to create an event from.
    :returns: Event file

    """
    event = Event()
    event.name = task['description']
    event.uid = task['uuid']
    # task and event must have same
    # event.begin = datetime.datetime.now()
    # event.end = datetime.datetime.now()+1


def next_sunday():
    """Get future sundays.
    :returns: List of future sundays.

    """
    today = datetime.datetime.today()
    month = today.month
    year = today.year

    sundays = list()
    for sunday in month_sundays(year, month):
        sundays.append(sunday)


def month_sundays(year, month):
    """Yields sundays for current month.
    :returns: List of future sundays.

    """
    date_sun = date(year, month, 1)
    date_sun += timedelta(days=6 - date_sun.weekday())
    while date_sun.year == year and date_sun.month == month:
        yield date_sun
        date_sun += timedelta(days=7)



def event_task_status(task):
    """Check if task on calendar is done.

    :task: Task class to check on calendar.
    :returns: True/False

    """
    # TODO: Check status of Event Task
    print(task)


def event_task_amend(task, calendar):
    """Amend the calendar task.

    :taks: Task class to change.
    :calendar: Calendar class to configure.
    :returns: New calendar event.

    """
    # TODO: Amend Task Event and Task
    print(task, calendar)
