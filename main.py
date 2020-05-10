"""
File: main.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: TaskKhalReschedulWarrior.
"""

import configparser

from constants import CONFIG_FILE
# from constants import DAY

# from events import next_days
from events import create_events
# from events import add_time

from tasks import load_tasks
# from tasks import scheduled_tasks
from tasks import overdue_tasks
from tasks import not_date_tasks
from tasks import load_tw_config

from logger import logger
from helpers import sort_task_urgency
# from helpers import execute


def main(task_config, khal_config):
    """TaskKhalReschedulWarrior.

    :task_config: TaskWarrior configuration.
    :khal_config: Khal configuration.
    :returns: True/False

    """
    # TODO: Khal logic
    # TODO: Set khal proper days
    logger.debug(khal_config)
    config = load_tw_config()

    projects = list(config.get('uda.trsw.projects'))
    print(projects)
    return

    tasks = load_tasks(task_config)
    tasks.sort(key=sort_task_urgency, reverse=True)

    # tasks_sched = scheduled_tasks(tasks)
    # events_sched = create_events(tasks_sched)
    nodates_tasks = overdue_tasks(tasks) + not_date_tasks(tasks)
    for task in nodates_tasks:
        if "lab" in task['project']:
            print(task)

    # create_events(nodates_tasks, khal_config)

    # execute(khal_config, cal_sundays)
    # execute(khal_config, cal_mondays)
    # execute(khal_config, cal_wednesdays)


if __name__ == "__main__":
    CONFIG = configparser.ConfigParser()
    CONFIG.read(CONFIG_FILE)
    TASK_CONF = list()
    TASK_CONF.append(CONFIG['TaskConfig']['TaskDir'])
    TASK_CONF.append(CONFIG['TaskConfig']['TaskProjects'].split(','))

    KHAL_CONF = list()
    # KHAL_CONF.append(CONFIG['KhalConfig']['KhalDir'])
    KHAL_CONF.append(CONFIG['KhalConfig']['KhalCalendar'])

    main(task_config=TASK_CONF, khal_config=KHAL_CONF)
