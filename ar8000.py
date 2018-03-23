# -*- coding: utf-8 -*-
#!#!/usr/bin/env python
"""The user interface for our app"""
 
import os, sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow 

# from PyQt5 import QtGui
import daiquiri
import daiquiri.formatter
import platform
import logging

import qtmodern
import qtmodern.styles
import qtmodern.windows

from logging.handlers import SocketHandler

log = logging.getLogger('Root logger')
log.setLevel(1)  # to send all messages to cutelog
socket_handler = SocketHandler('127.0.0.1', 19996)  # default listening address
log.addHandler(socket_handler)
log.info('Hello world!')

daiquiri.setup(level=logging.INFO, outputs=(
    daiquiri.output.Stream(formatter=daiquiri.formatter.ColorFormatter(
        fmt=(daiquiri.formatter.DEFAULT_FORMAT +
             " [%(subsystem)s is %(mood)s]"))),
    ))

# logger = daiquiri.getLogger()
logger = daiquiri.getLogger(__name__, subsystem="example")
daiquiri.setup(level=logging.INFO, outputs=(
    daiquiri.output.Stream(formatter=daiquiri.formatter.ColorFormatter(
        fmt="%(asctime)s  %(lineno)d [%(levelname)s] "
        "%(name)s -> %(message)s")),
    ))

logger = daiquiri.getLogger(__name__)
logger.info("Running Version: " + platform.python_version() + " " +os.getcwd())

def main():
    app = QApplication(sys.argv)
    print(app)
    main_window = MainWindow()
    # main_window.show()
    
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(main_window)
    mw.show()
    sys.exit(app.exec_())
    # It's exec_ because exec is a reserved word in Python


if __name__ == "__main__":
    main()

