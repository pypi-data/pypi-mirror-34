# -*- coding:utf-8 -*-
import logging
import weakref

from .output import get_output_obj

_REE_LOGGERS = weakref.WeakValueDictionary()

def get_logger(name=None, outputs=["stdout"], level=logging.INFO):
    if not name:
        name = "root"
    logger = _REE_LOGGERS.get(name)
    if not logger:
        logger = _init_logger(name, outputs, level)
        _REE_LOGGERS[name] = logger

    return logger


def _init_logger(name, outputs, level):
    logger = logging.getLogger(name)
    [logger.removeHandler(handler) for handler in logger.handlers]

    for item in outputs:
        output_obj = get_output_obj(item)
        output_obj.add_to_logger(logger)

    logger.setLevel(level)
    return logger
