#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = 'Copyright 2020'

__all__ = [
    'install_logger',
    'get_logger',
    'exceptstr',
    'demonstrate_logger',
]

import logging

import coloredlogs
import verboselogs

class Logger:

    fmt = '%(asctime)s %(name)16.16s:%(lineno)-4d %(levelname)8s %(message)s'
    field_styles = {
        'asctime': { 'color': 'green', 'faint': True, },
        'name': { 'color': 'cyan', 'faint': True, },
        'levelname': { 'color': 'black', 'bold': True, },
    }
    level_styles = {
        'spam': { 'color': 'magenta', 'faint': True, },
        'debug': { 'color': 'blue', },
        'verbose': { 'color': 'magenta', },
        'info': { 'color': 'cyan', },
        'notice': { 'color': 'cyan', 'bold': True, },
        'warning': { 'color': 'yellow', 'faint': True, },
        'io': { 'color': 172, },
        'success': { 'color': 'green', 'bold': True, },
        'error': { 'color': 'red', 'bold': True, },
        'critical': { 'background': 'red', 'bold': True, },
    }

    @classmethod
    def install_logger(cls):
        verboselogs.add_log_level(32, 'IO')
        setattr(verboselogs.VerboseLogger, 'fin',   lambda self, name, *args, **kw: self._log(32, '<< '+name, args, **kw))
        setattr(verboselogs.VerboseLogger, 'fout',  lambda self, name, *args, **kw: self._log(32, '>> '+name, args, **kw))
        setattr(verboselogs.VerboseLogger, 'fcp',   lambda self, src, dst, *args, **kw: self._log(32, src+' => '+dst, args, **kw))
        setattr(verboselogs.VerboseLogger, 'flink', lambda self, src, dst, *args, **kw: self._log(32, src+' <- '+dst, args, **kw))

        verboselogs.install()
        coloredlogs.install(level=5, fmt=cls.fmt, field_styles=cls.field_styles, level_styles=cls.level_styles)

    @staticmethod
    def get_logger(modname):
        modname = modname[-16:]
        return logging.getLogger(modname)

    @staticmethod
    def exceptstr(e):
        return f'{e.__class__.__name__}: {e}'

    @classmethod
    def demonstrate_logger(cls, logger=None):
        if not logger:
            logger = get_logger(__name__)
        for name in cls.level_styles:
            level = coloredlogs.level_to_number(name)
            logger.log(level, f'message with level {name} ({level})')

install_logger = Logger.install_logger
get_logger = Logger.get_logger
exceptstr = Logger.exceptstr
demonstrate_logger = Logger.demonstrate_logger

if __name__ == '__main__':
    install_logger()
    demonstrate_logger()
