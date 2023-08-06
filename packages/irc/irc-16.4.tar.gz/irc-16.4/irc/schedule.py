import abc

import six

from tempora import schedule

__metaclass__ = type


@six.add_metaclass(abc.ABCMeta)
class IScheduler:
    @abc.abstractmethod
    def execute_every(self, period, func):
        "execute func every period"

    @abc.abstractmethod
    def execute_at(self, when, func):
        "execute func at when"

    @abc.abstractmethod
    def execute_after(self, delay, func):
        "execute func after delay"

    @abc.abstractmethod
    def run_pending(self):
        "invoke the functions that are due"


class DefaultScheduler(schedule.InvokeScheduler, IScheduler):
    def execute_every(self, period, func):
        self.add(schedule.PeriodicCommand.after(period, func))

    def execute_at(self, when, func):
        self.add(schedule.DelayedCommand.at_time(when, func))

    def execute_after(self, delay, func):
        self.add(schedule.DelayedCommand.after(delay, func))
