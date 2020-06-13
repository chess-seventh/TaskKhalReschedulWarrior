"""
File: main.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: TaskKhalReschedulWarrior.
"""
from taskw import TaskWarrior as TaskW

from events import create_events

from tasks import load_tasks
from tasks import overdue_tasks
from tasks import not_date_tasks


from logger import logger
from helpers import sort_task_urgency


def main():
    """TaskKhalReschedulWarrior.

    :task_config: TaskWarrior configuration.
    :khal_config: Khal configuration.
    :returns: True/False

    """
    # TODO: Khal logic
    # TODO: Set khal proper days

    task_war = TaskW(config_filename="./taskrcdir")
    tw_config = task_war.load_config()
    tw_config_location = tw_config['data']['location']
    tw_projects = tw_config['uda.trsw.projects'].split(',')
    khal_location = tw_config['uda.calendar.location']
    khal_config = tw_config['uda.khal.config']

    print(tw_projects)
    print(khal_location)
    print(khal_config)
    return

    tasks = load_tasks(tw_config_location)
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
    main()
