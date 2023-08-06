# -*- coding:utf-8 -*-
import sys
import logging
import logging.handlers
from .formatter import TEXT_FORMATTER
from .handler import TTYHandler
from .utils import get_log_file_path


class Output(object):
    def __init__(self, handler, formatter=TEXT_FORMATTER, level=logging.INFO):
        self.handler = handler
        self.handler.setFormatter(formatter)
        self.handler.setLevel(level)

    def add_to_logger(self, logger):
        logger.addHandler(self.handler)


class Stream(Output):
    def __init__(self, stream=sys.stdout, formatter=TEXT_FORMATTER, level=logging.INFO):
        super(Stream, self).__init__(TTYHandler(stream), formatter, level)


class File(Output):
    def __init__(self, filename=None, formatter=TEXT_FORMATTER, level=logging.INFO):
        log_file_path = get_log_file_path(file_name=filename)
        handler = logging.FileHandler(filename=log_file_path)
        super(File, self).__init__(handler, formatter, level)


TO_STDOUT = Stream()
TO_FILE = File()

OUT_MAPPING = {
    "stdout": TO_STDOUT,
    "file": TO_FILE
}