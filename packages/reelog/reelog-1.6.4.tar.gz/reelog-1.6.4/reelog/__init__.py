# -*- coding:utf-8 -*-
import logging
import weakref

from .output import OUT_MAPPING

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
    outputs = [OUT_MAPPING.get(item, None) for item in outputs]
    if None in outputs:
        raise ValueError

    logger = logging.getLogger(name)
    [logger.removeHandler(handler) for handler in logger.handlers]

    for out in outputs:
        out.add_to_logger(logger)

    logger.setLevel(level)
    return logger
