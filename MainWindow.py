#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:22:53 2018

@author: chrissy
"""

from __future__ import print_function
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QAbstractItemView
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
import daiquiri
import logging
from radio import connect
from db_list import database_list
# from decode_response import decode
from MainWindow_ui import Ui_MainWindow
daiquiri.setup()
logger = daiquiri.getLogger()
daiquiri.setup(level=logging.INFO, outputs=(
    daiquiri.output.Stream(formatter=daiquiri.formatter.ColorFormatter(
        fmt="%(asctime)s %(lineno)d [%(levelname)s] "
        "%(name)s -> %(message)s")),
    ))

logger = daiquiri.getLogger(__name__)
#`from PyQt4.QtGui import *

#import os
#import sys

#from decode_response import decode_responsea
LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

logger.info("here in MainWindow.py")

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        #self.value = value
        QMainWindow.__init__(self, parent=None)
        
        self.setupUi(self)
        # Select whole row on click
        self.tableWidget_Station.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # Connect signal for app finish
        self.radioButton_CW.clicked.connect(self.textEdit_PI.selectAll)
        self.pushButton_RX.clicked.connect(self.mymethod_rx)
        self.pushButton_RX.clicked.connect(self.mymethod_rx) # signal/slot connection
        self.pushButton_RF.clicked.connect(self.mymethod_rf) # signal/slot connection
        self.pushButton_SS.clicked.connect(self.mymethod_ss) # signal/slot connection
        self.pushButton_VA.clicked.connect(self.mymethod_va) # signal/slot connection
        self.pushButton_VB.clicked.connect(self.mymethod_vb) # signal/slot connection
        self.pushButton_Quit.clicked.connect(self.mymethod_quit) # signal/slot connection
        self.pushButton_Refresh.clicked.connect(self.mymethod_refresh) # signal/slot connection
        self.pushButton_ByHand.clicked.connect(self.mymethod_byhand) # signal/slot connection
        self.pushButton_PA.clicked.connect(self.mymethod_pa) # signal/slot connection
        self.pushButton_PI.clicked.connect(self.mymethod_pi) # signal/slot connection
        self.radioButton_WFM.clicked.connect(self.mymethod_wfm)
        self.radioButton_NFM.clicked.connect(self.mymethod_nfm)
        self.radioButton_AM.clicked.connect(self.mymethod_am)
        self.radioButton_USB.clicked.connect(self.mymethod_usb)
        self.radioButton_LSB.clicked.connect(self.mymethod_lsb)
        self.radioButton_CW.clicked.connect(self.mymethod_cw)
        self.checkBox_AutoStepMode.stateChanged.connect(self.mymethod_AutoStepMode)
        self.radioButton_AU.clicked.connect(self.mymethod_rx)
        self.radioButton_mute_off.clicked.connect(self.mymethod_rx)
        self.radioButton_mute_on.clicked.connect(self.mymethod_rx)
        self.radioButton_mute_normal.clicked.connect(self.mymethod_rx)
        self.pushButton_LC.clicked.connect(self.mymethod_lc)
        self.pushButton_LM.clicked.connect(self.mymethod_lm)
        self.doubleSpinBox_RF.valueChanged.connect(self.mymethod_rf)
        self.dial.valueChanged.connect(self.mymethod_rx)
        self.pushButton_DD.clicked.connect(self.mymethod_dd)
        self.pushButton_Refresh.clicked.connect(self.refresh_all)
        self.tableWidget_Station.clicked.connect(self.tableWidget_Station_clicked)
        self.refresh_all()
        
        
    def refresh_all(self, readonly=False):
        station_db = database_list()
        station_db.list_it(self.tableWidget_Station)
        logger.info("In Refresh_All")
        #self.ar8000 = radio()
        self.ar8000 = connect()
        # ar8000.connect()
        SerialStatus = self.ar8000.initialise()
        if (SerialStatus):
            self.label_error.setText("<b><font color=green>Serial Connection Attached</font></b>")
        else:
            self.label_error.setText("<b><font color=red>No Connection</font></b>")
            return (None)
        logger.info("Serial Connection Status:" +str(SerialStatus))
        #
        sCommand = "RX"
        SerialResponse = self.ar8000.openit(sCommand)
        print(len(SerialResponse))
        if (len(SerialResponse) != 0 ):
            self.label_ResponseBack.setText("<b><font color=green>Data Received</font></b>")
        else:
            self.label_ResponseBack.setText("<b><font color=red>No Data Received, power up ?</font></b>")
            return (None)
        #
        logger.info("Serial Connection Status: " +str(SerialResponse))        #
        #label_ResponseBack
        #
        # print("here: " + type(serialResponse))
        # logger.info("Serial Connection Status Response:" +len(serialResponse))
        #
        
    
    def tableWidget_Station_clicked(self):
        station_db = database_list()
        station_db.list_it(self.tableWidget_Station)
        print("\n")
        logger.info("Column Count" +str(self.tableWidget_Station.columnCount()))
        for column in range(self.tableWidget_Station.columnCount()):
            itemText = self.tableWidget_Station.item(self.tableWidget_Station.currentRow(), column).text()
            logger.info("Item Text - " + itemText)
       
    def mymethod_dd(self, readonly=True):
        sCommand = "DD"
        self.serialResponse = self.ar8000.openit(sCommand)
        logger.info("serialResponseDD %s: " % (self.serialResponse))


    def mymethod_xm(self, readonly=True):
        sCommand = "XM"
        serialResponse = self.ar8000.openit(sCommand)
        logger.info("serialResponseXM %s: " % (serialResponse))
        
    def mymethod_AutoStepMode(self):
        sCommand = 'AU1' if self.checkBox_AutoStepMode.isChecked() else 'AU0'
        self.serialResponse = self.ar8000.openit(sCommand)
        sCommand = "AU"
        self.serialResponse = self.ar8000.openit(sCommand)
        logger.info("AutoStepMode" + self.serialResponse)
        self.label_au1_response.setText(self.serialResponse)
    
    def mymethod_changerf(self, readonly=True):
        data = float(self.doubleSpinBox_RF.value())
        sCommand = "RF"
        sCommand += str(data)
        serialResponse = self.ar8000.openit(data)
        self.label_serialResponse.setText(serialResponse)
        logger.info("--- now doing LM ----")
        self.mymethod_lm()

    def mymethod_change_dial(self, readonly=True):
        logger.info("ChangeDial")
        self.addActionreadonly = False
        data = float(self.dial.value())
        sCommand = "RF"
        sCommand += str(data)
        serialResponse = self.ar8000.openit(data)
        logger.info("dial %s" % (serialResponse))
        self.label_serialResponse.setText(serialResponse)

    def mymethod_lc(self, readonly=False, openLC="LC0000000000"):
        '''
        This updates the progress bar
        '''
        sCommand = "LC\n"
        self.openLC = self.ar8000.openit(sCommand)
        logger.info(self.openLC)
        logger.info(len(openLC))
        if (len(openLC) == 12):
            self.openLC = self.ar8000.openit(data)
        logger.info("openLC %s " % self.openLC)
        z = openLC.strip('LC')
        hex = z[0:2]
        logger.infi("its hex %s" % (hex))
        if (not hex):
            logger.error("its not hex")
            openLC = self.ar8000.openit(data)
            z = openLC.strip('LC')
            hex = z[0:2]
        dec = (hex, 16)
        logger.info("dec %s " % (dec))
        self.progressBar_LC.setValue(32)

    def mymethod_lm(self, readonly=False):
        '''
        Responds with S-meter reading
        LMnn
        00-3F = squelch open 0-63 dec
        80-BF - squelch closed 128-191 dec
        '''
        sCommand = "LM"
        serialResponse = self.ar8000.openit(sCommand)
        logger.info("LM response: %s " % (serialResponse))
        z = serialResponse.strip('LM')
        z = int(z, 16)
        logger.info("LM decimal: " +str(z))
        smeter_percentage = (100/63)*z
        logger.info("smeter_percentage: " +str(smeter_percentage))
        if (z >= 128):
            logger.info("Squelch Closed")
        else:
            logger.info("Squelch Open")
        self.progressBar_LC.setValue(z)




    def mymethod_au(self, readonly=False):
        sCommand = "AU1"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)
        
    def mymethod_wfm(self, readonly=False):
        sCommand = "MD0"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)

    def mymethod_nfm(self, readonly=False):
        sCommand = "MD1"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)

    def mymethod_am(self, readonly=False):
        sCommand = "MD2"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)

    def mymethod_usb(self, readonly=False):
        sCommand = "MD3"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)

    def mymethod_lsb(self, readonly=False):
        sCommand = "MD4"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)

    def mymethod_cw(self, readonly=False):
        sCommand = "MD5"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)
 
    def mymethod_rx(self, readonly=False):
        response = []
        sCommand = 'RX'
        sResponse = self.ar8000.openit(sCommand)
        logger.info("RX data %s" % (sResponse))
        response = sResponse.split(" ")
        logger.info("here")
        return(response)
        #logger.info("response list %s " % (str(response)))
        #print(len(response))

    def mymethod_byhand(self, readonly=False):
        '''
        By hand can only be write, it takes whatever command and data you have and sendsit.
        '''
        ByHand = self.textEdit_ByHand
        data = ByHand.toPlainText()
        openByHand = self.ar8000.openit(data)
        logger.info("open ByHand in MainWindow %s" % (openByHand))
        self.label_radio_response.setText(openByHand)

    def mymethod_quit(self, readonly=False):
        logger.info("MainWindow.py hit the pushButton_Quit")
        #sys.exit(app.exec_())
        self.close()
    
    def mymethod_refresh(self, readonly=False):
        '''
        Slot documentation goes here.
        '''
        logger.info("MainWindow.py hit the pushButton_Refresh")
        self.refresh_all()
        
    def mymethod_rf(self, readonly=False, increment=0):
        '''
        Set Frequency - Can only be write
        Comes back with SS RF0093200000 ST100000  AU1 MD0 AT0 TTBAND 2
        '''
        logger.info("SpinBox Value: %s " % (self.doubleSpinBox_RF.value()))
        value = self.doubleSpinBox_RF.value()
        sCommand = "RF"
        sCommand += str(value)
        logger.info("sCommand: " +sCommand)
        serialResponse = self.ar8000.openit(sCommand)
        logger.info("openRF in MainWindow %s" % (serialResponse))
        self.doubleSpinBox_RF.setValue(value)
        self.label_serialResponse.setText(serialResponse)
        self.mymethod_lm()
        
    def mymethod_ss(self, readonly=False):
        '''
        It comes back with SS RF0093200000 ST100000  AU1 MD0 AT0 TTBAND 2 
        '''
        data = 'SS'
        serialResponse = self.ar8000.openit(data)
        logger.info("SS %s" % (serialResponse))
        results = serialResponse.split()
        logger.info(results)
        self.label_serialResponse.setText(serialResponse)

    def mymethod_va(self, readonly=False):
        '''
        Slot documentation goes here.
        '''
        sCommand = "VA"
        data = self.textEdit_input_freq_VA
        data = data.toPlainText()
        data = float(data)
        sCommand += str(data)
        serialResponse = self.ar8000.openit(sCommand)
        logger.info("openVA in MainWindow %s" % (serialResponse))
        self.label_serialResponse.setText(serialResponse)

    def mymethod_vb(self):
        '''
        Slot documentation goes here.
        '''
        data = 'VB'
        serialResponse = self.ar8000.openit(data)
        logger.info("openVB in MainWindow %s" % (serialResponse))
        self.label_serialResponse.setText(serialResponse)
        
    def mymethod_pa(self, readonly=False):
        '''
        Set Delay for power save mode
        '''
        logger.info("readonly PA %s " % (readonly))
        sCommand = "PA"
        if readonly:
            serialResponse = self.ar8000.openit(sCommand)
            logger.info("serial reponse %s" % serialResponse)
            self.textEdit_PA.setText(serialResponse)
        else:
            data = self.textEdit_PA
            data = data.toPlainText()
            data = str(data)
            sCommand += data
            sCommand = sCommand.rstrip()
            logger.info("its PA data: %s" % (sCommand))
            
            type(sCommand)
            logger.info(sCommand)
            #serialResponse = self.rad.openit(sCommand)
            serialResponse = self.ar8000.openit(sCommand)           
            logger.info(serialResponse)
            #response = serialResponse.toPlainText()
            logger.info("openPA in MainWindow %s" % (serialResponse))
    
         
    def mymethod_pi(self, readonly=False):
        '''
        Slot documentation goes here.
        '''
        logger.info("readonly PI %s " % (readonly))
        sCommand = "PI"
        if (readonly):
            serialResponse = self.ar8000.openit(sCommand)
            logger.info("openPI in MainWindow %s" % (serialResponse))
            self.textEdit_PI.setText(serialResponse)
        else:
            data = self.textEdit_PI
            data = data.toPlainText()
            data = str(data)
            sCommand += data
            sCommand = sCommand.rstrip()
            logger.info("its PI data: %s" % (data))
            serialResponse = self.ar8000.openit(data)
            logger.info("openPI in MainWindow %s" % (serialResponse))


    def mymethod_mute_off(self, readonly=False):
        sCommand = "MC0"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)
        logger.info("mute off")

    def mymethod_mute_on(self, readonly=False):
        sCommand = "MC1"
        openMD = self.ar8000.openit(sCommand)
        logger.info(openMD)
        logger.info("mute on")

    def mymethod_mute_normal(self, readonly=False):
        sCommand = "MC2"
        openMD = self.ar8000.openit(sCommand)
