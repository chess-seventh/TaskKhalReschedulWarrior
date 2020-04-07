# TaskKhalReschedulWarrior

TaskWarrior rescheduler into the Khal calendar.

 - [Taskwarrior](https://taskwarrior.org)
 - [tasklib](https://github.com/robgolding/tasklib)
 - [khal](https://github.com/pimutils/khal)


# Project

In order to get my tasks in my calendar to organize my "lazy" sundays with stuff I'd like to do.

This project is still a Work In Progress...


# Install

You may need python `virutalenv`.


```bash
mkvirtualenv taskkhalreschedulwarrior
pip install -r requirements
```

# Configuration

The `config.ini` file is where the project will fetch the data of TaskWarrior and Khal.


## TaskConfig

`TaskDir`: Is the directory where you TaskWarrior data is stored.

`TaskProjects`: A list of the TaskWarrior projects you'd like to work on during your "lazy" sundays.

## KhalConfig

__This part is still WIP__

`KhalDir`: Directory of Khal

`KhalCalendar`: To which Khal Calendar the `EventTasks` should be scheduled.


# Usage

```
python main.py
```

# TODO & WIP & IDEAS

## TODO

There are still many parts to improve and to do, here's a quick list:

 - `./main.py`:    # TODO: Khal logic
 - `./main.py`:    # TODO: Check what directory needs to be set.
 - `./events.py`:  # TODO: Check status of Event Task
 - `./events.py`:  # TODO: Amend Task Event and Task
 - `./tasks.py`:   # TODO: Fix filtering of tasks
 - `./tasks.py`:   # TODO: Return Scheduled Tasks

Most likely this project could be set a TaskWarrior [Hook](https://taskwarrior.org/docs/hooks2.html), but the current approach is not fit for it... yet.


## WIP

 - get tasks
 - filter tasks with due dates
 - check overdue tasks
 - add due dates to tasks without
 - get calendar events
 - compate calendar events with tasks with due dates
 - check for overdue tasks-events and postpone them to the end


### IDEAS

 - prioritize tasks scheduled date based on urgency flag

## Contributing

**Note:**
This project is released with a Contributor Code of Conduct.
By participating in this project **you agree** to abide by its terms.
See the [CODE OF CONDUCT.md](CODE_OF_CONDUCT.md) file for details.

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Authors

* **Chess Seventh** - Maintainer - [chess-seventh](https://github.com/chess-seventh)

## License

This project is licensed under the GNU General Public License -
see the [LICENSE.md](LICENSE.md) file for details.
