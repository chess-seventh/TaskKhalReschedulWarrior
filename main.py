"""
File: main.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: TaskKhalReschedulWarrior.
"""

import configparser
from constants import CONFIG_FILE
from tasks import load_tasks
from helpers import sort_task_urgency


def main(task_config, khal_config):
    """TaskKhalReschedulWarrior.

    :task_config: TaskWarrior configuration.
    :khal_config: Khal configuration.
    :returns: True/False

    """
    # TODO: Khal logic
    print(khal_config)

    tasks = load_tasks(task_config)
    tasks.sort(key=sort_task_urgency, reverse=True)

    for task in tasks:
        if task['scheduled'] and task['due']:
            print(task, task['scheduled'], task['due'])


if __name__ == "__main__":
    CONFIG = configparser.ConfigParser()
    CONFIG.read(CONFIG_FILE)
    TASK_CONF = list()
    TASK_CONF.append(CONFIG['TaskConfig']['TaskDir'])
    TASK_CONF.append(CONFIG['TaskConfig']['TaskProjects'].split(','))
    print(TASK_CONF)

    # TODO: Check what directory needs to be set.
    KHAL_CONF = list()
    KHAL_CONF.append(CONFIG['KhalConfig']['KhalDir'])
    KHAL_CONF.append(CONFIG['KhalConfig']['KhalCalendar'])
    print(KHAL_CONF)

    main(task_config=TASK_CONF, khal_config=KHAL_CONF)
