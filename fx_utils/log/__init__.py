import logging

from fx_utils.metaclasses import Singleton


def get_logger(name):
    log_manager = LogManager()
    return log_manager.get_logger(name)


class LogManager(object, metaclass=Singleton):

    def __init__(self):
        self.loggers = {}

    def get_logger(self, name):
        if name in self.loggers:
            return self.loggers[name]
        else:
            logger = MyLogger(name)
            return logger


class MyLogger(logging.Logger):

    def __init__(self, name, level=logging.NOTSET):
        super(MyLogger, self).__init__(name, level)

    def _message(self):
        return

