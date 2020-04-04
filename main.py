"""
File: main.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: TaskKhalReschedulWarrior.
"""

import configparser
from constants import CONFIG_FILE
from constants import DAY
from events import next_days
from events import create_events
from events import add_time
from tasks import load_tasks
from tasks import scheduled_tasks
from tasks import overdue_tasks
from tasks import not_date_tasks
from logger import logger
from helpers import sort_task_urgency
import datetime


def main(task_config, khal_config):
    """TaskKhalReschedulWarrior.

    :task_config: TaskWarrior configuration.
    :khal_config: Khal configuration.
    :returns: True/False

    """
    # TODO: Khal logic
    logger.debug(khal_config)

    tasks = load_tasks(task_config)
    tasks.sort(key=sort_task_urgency, reverse=True)

    tasks_sched = scheduled_tasks(tasks)
    tasks_overdue = overdue_tasks(tasks)

    # logger.debug("scheduled")
    # logger.debug(tasks_sched)

    # logger.debug("overdue")
    # logger.debug(tasks_overdue)

    no_date_t = not_date_tasks(tasks)
    sundays = list(map(add_time, next_days(DAY['SUN'])))
    cal = create_events(no_date_t, sundays)
    print(cal)


if __name__ == "__main__":
    CONFIG = configparser.ConfigParser()
    CONFIG.read(CONFIG_FILE)
    TASK_CONF = list()
    TASK_CONF.append(CONFIG['TaskConfig']['TaskDir'])
    TASK_CONF.append(CONFIG['TaskConfig']['TaskProjects'].split(','))

    # TODO: Set proper directory.
    KHAL_CONF = list()
    KHAL_CONF.append(CONFIG['KhalConfig']['KhalDir'])
    KHAL_CONF.append(CONFIG['KhalConfig']['KhalCalendar'])

    main(task_config=TASK_CONF, khal_config=KHAL_CONF)
