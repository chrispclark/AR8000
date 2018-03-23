#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:37:53 2018

@author: chrissy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from db_create import Radio, Base
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
import daiquiri
import logging
from MainWindow_ui import Ui_MainWindow

daiquiri.setup()
logger = daiquiri.getLogger()
daiquiri.setup(level=logging.INFO, outputs=(
    daiquiri.output.Stream(formatter=daiquiri.formatter.ColorFormatter(
        fmt="%(asctime)s %(lineno)d [%(levelname)s] "
        "%(name)s -> %(message)s")),
    ))

logger = daiquiri.getLogger(__name__)



class database_list():
    def list_it(self,ss):
        self.tableWidget_Station = ss
        
        engine = create_engine('sqlite:///radio.db')
        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        Base.metadata.bind = engine
        
        DBSession = sessionmaker(bind=engine)
        # A DBSession() instance establishes all conversations with the database
        # and represents a "staging zone" for all the objects loaded into the
        # database session object. Any change made against the objects in the
        # session won't be persisted into the database until you call
        # session.commit(). If you're not happy about the changes, you can
        # revert all of them back to the last commit by calling
        # session.rollback()
        session = DBSession()
        
        # print("----> order_by(id):")
        query = session.query(Radio).order_by(Radio.id)
        
        x = 0
        self.tableWidget_Station.setRowCount(4)
        for row in query.all():
            # print(row)
            #print(row.channel_name, row.channel_frequency, row.channel_band)
                
            self.tableWidget_Station.setHorizontalHeaderLabels(["Station", "Frequency", "Band"])
            self.tableWidget_Station.setItem(x, 0, QTableWidgetItem(row.channel_name))
            self.tableWidget_Station.setItem(x, 1, QTableWidgetItem(row.channel_frequency))
            self.tableWidget_Station.setItem(x, 2, QTableWidgetItem(row.channel_band))
            x =x +1
        self.tableWidget_Station.resizeRowsToContents()
        self.tableWidget_Station.resizeColumnsToContents()
        
        
            
def main():
    sammy = database_list()
    sammy.list_it()

if __name__ == "__main__":
    main()