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
from ics import Calendar
from logger import logger
# from helpers import format_date
from helpers import execute


def create_events(tasks, khal_config):
    """Create an Event based on task parameters.

    :task: Task to create an event from.
    :returns: Event file

    """
    today = datetime.datetime.now()
    today_day = today.date()
    next_day = datetime.datetime.combine(today_day, datetime.time(8, 30, 0))
    for task in tasks:
        next_day += datetime.timedelta(days=1)
        calendar = Calendar()
        event = Event()
        event.name = task['description']
        event.uid = task['uuid']
        # event.begin = format_date(next_day)
        event.begin = next_day
        calendar.events.add(event)

        ics_name = "./ics/" + task['uuid'] + ".ics"
        with open(ics_name, 'w') as cal_file:
            cal_file.writelines(calendar)

        execute(khal_config, ics_name)


def next_days(day_of_week):
    """Get future days.
    :returns: List of future days.
    """
    today = datetime.datetime.today()
    month = today.month
    year = today.year

    chosen_day = list()
    for sunday in month_chosen_day(year, month, day_of_week):
        chosen_day.append(sunday)
    return chosen_day


def month_chosen_day(year, month, week_day):
    """Yields sundays for current month.

    :year: Year of the event to be set.
    :month: Month of the event to be set.
    :week_day: Day of the week (MON/SUN...) of the event to be set.
    :returns: List of future week days to be scheduled.

    """
    # TODO: Fix chosen day variable to be pickedup.
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

    :tasks: task class to change.
    :calendar: calendar class to configure.
    :returns: new calendar event.

    """
    # TODO: Amend Task Event and Task
    logger.debug(task, calendar)


def add_time(date):
    """Add time to date.

    :hour: Hour.
    :minutes: Minutes
    :returns: The modified new date.

    """
    hour = 7
    minutes = 30
    new_date = datetime.datetime.combine(date, datetime.time(hour, minutes))
    return new_date
