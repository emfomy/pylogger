#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'

__all__ = [ 'install_logger', 'demonstrate_logger' ]

import builtins
import inspect
import logging

import coloredlogs
import verboselogs

class Logger:

    fmt = '%(asctime)s %(name)24.24s:%(lineno)-4d %(levelname)8s %(message)s'

    field_styles = {
        'asctime': {'color': 'green', 'faint': True},
        'name': {'color': 'cyan', 'faint': True},
        'levelname': {'color': 'black', 'bold': True},
    }

    level_styles = {
        'spam': {'color': 'magenta', 'faint': True},
        'debug': {'color': 'blue'},
        'verbose': {'color': 'magenta'},
        'info': {'color': 'cyan'},
        'notice': {'color': 'cyan', 'bold': True},
        'warning': {'color': 'yellow', 'bold': True},
        'success': {'color': 'green', 'bold': True},
        'error': {'color': 'red', 'bold': True},
        'critical': {'background': 'red', 'bold': True},
    }

    @classmethod
    def install_logger(cls):
        verboselogs.install()
        coloredlogs.install(level=5, fmt=cls.fmt, level_styles=cls.level_styles, field_styles=cls.field_styles)
        builtins.logger = cls.logger
        builtins.exceptstr = cls.exceptstr

    @staticmethod
    def logger():
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        name = getattr(mod, '__name__', '')
        return logging.getLogger(name)

    @staticmethod
    def exceptstr(e):
        return f'{e.__class__.__name__}: {e}'

    @classmethod
    def demonstrate_logger(cls):
        for name in cls.level_styles:
            level = coloredlogs.level_to_number(name)
            logger().log(level, f'message with level {name} ({level})')

install_logger = Logger.install_logger
demonstrate_logger = Logger.demonstrate_logger

if __name__ == '__main__':
    install_logger()
    demonstrate_logger()
