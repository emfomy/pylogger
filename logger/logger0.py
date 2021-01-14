#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Mu Yang <http://muyang.pro>'
__copyright__ = 'Copyright 2020'

__all__ = [
    'demonstrate_logger',
    'exceptstr',
    'get_logger',
    'install_logger',
]

import logging

import coloredlogs
import verboselogs

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

def install_logger():
    verboselogs.add_log_level(32, 'IO')
    setattr(verboselogs.VerboseLogger, 'fin',   lambda self, name, *args, **kw: self._log(32, '<< '+name, args, **kw))
    setattr(verboselogs.VerboseLogger, 'fout',  lambda self, name, *args, **kw: self._log(32, '>> '+name, args, **kw))
    setattr(verboselogs.VerboseLogger, 'fcp',   lambda self, src, dst, *args, **kw: self._log(32, src+' => '+dst, args, **kw))
    setattr(verboselogs.VerboseLogger, 'flink', lambda self, src, dst, *args, **kw: self._log(32, src+' <- '+dst, args, **kw))

    verboselogs.install()
    coloredlogs.install(level=5, fmt=fmt, field_styles=field_styles, level_styles=level_styles)

def get_logger(modname):
    modname = modname[-16:]
    return logging.getLogger(modname)

def exceptstr(e):
    return f'{e.__class__.__name__}: {e}'

def demonstrate_logger(logger = None):
    if not logger:
        logger = get_logger(__name__)
    for name in level_styles:
        level = coloredlogs.level_to_number(name)
        logger.log(level, f'message with level {name} ({level})')

install_logger()
