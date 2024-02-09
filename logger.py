import logging
import traceback

from utils import grey, cyan, yellow, red, bold


class CustomTerminalFormatter(logging.Formatter):
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    reset = '\033[0m'

    FORMATS = {
        logging.DEBUG: grey(format) + reset,
        logging.INFO: cyan(format) + reset,
        logging.WARNING: yellow(format) + reset,
        logging.ERROR: red(format) + reset,
        logging.CRITICAL: bold(red(format)) + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class CustomFileFormatter(logging.Formatter):
    def format(self, record):
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        return formatter.format(record)


class SelectiveLogger:
    def __init__(self, terminal_logger, file_logger):
        self.term = terminal_logger
        self.file = file_logger

    def info(self, msg='', terminal=True):
        if terminal:
            self.term.info(msg)
        self.file.info(msg)

    def debug(self, msg='', terminal=True):
        if terminal:
            self.term.debug(msg)
        self.file.debug(msg)

    def warn(self, msg='', terminal=True):
        if terminal:
            self.term.warn(msg)
        self.file.warn(msg)

    def error(self, msg='', terminal=True):
        if terminal:
            self.term.error(msg)
        self.file.error(msg)

    def critical(self, msg='', terminal=True):
        if terminal:
            self.term.critical(msg)
        self.file.critical(msg)


def get_logger(log_path):
    term = logging.getLogger('space-fake').getChild('terminal')
    file = logging.getLogger('space-fake').getChild('file')

    sh = logging.StreamHandler()
    sh.setFormatter(CustomTerminalFormatter())

    fh = logging.FileHandler(log_path)
    fh.setFormatter(CustomFileFormatter())

    # link handler to logger
    term.addHandler(sh)
    file.addHandler(fh)

    # Set logging level to the logger
    term.setLevel(logging.DEBUG)
    file.setLevel(logging.DEBUG)

    return SelectiveLogger(term, file)


def log_continue(fn):
    def wrapped(log, *args, **kwargs):
        try:
            return fn(log, *args, **kwargs)
        except Exception as e:
            traceback.print_exception(e)
            log.error(str(e))
            return None

    return wrapped
