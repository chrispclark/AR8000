import serial
import logging
import daiquiri

daiquiri.setup()
logger = daiquiri.getLogger()
daiquiri.setup(level=logging.INFO, outputs=(
    daiquiri.output.Stream(formatter=daiquiri.formatter.ColorFormatter(
        fmt="%(asctime)s  %(lineno)d [%(levelname)s] "
        "%(name)s -> %(message)s")),
    ))

logger = daiquiri.getLogger(__name__)

#initialization and open the port
#possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

class connect():
    def __init__(self):
        self.ser = serial.Serial()

    def initialise(self):
        self.ser.port = "/dev/ttyUSB0"
        self.ser.baudrate = 9600
        self.ser.bytesize = serial.EIGHTBITS 	        #number of bits per bytes
        self.ser.parity = serial.PARITY_NONE 	        #set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE 	#number of stop bits
        #self.ser.timeout = None          		        #block read
        self.ser.timeout = 1           		                #non-block read
        #self.ser.timeout = 2              		                #timeout block read
        self.ser.xonxoff = False     		                #disable software flow control
        self.ser.rtscts = False     			        #disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False       		                #disable hardware (DSR/DTR) flow control
        self.ser.writeTimeout = 1    		                #timeout for write
        successSerialOpen = False
        logger.info("Serial Names = " + self.ser.name)
        
        try:
            self.ser.open()
        except serial.SerialException as e:
             self.ser.close()
             logger.error("There was a serial error, attempting to recover")
             successSerialOpen = False
         
        if self.ser.is_open:
            logger.info("Serial connection is available")
            successSerialOpen = True
            #self.openit("LC","LC")
            #return self.ser
        else:
            logger.error("Please Connect The Serial Cable")
            successSerialOpen = False
        return (successSerialOpen)

    def openit(self, command, data ="empty"):
        self.command = command+'\r\n'
        self.sendEncodedCommand = self.command.encode("ascii")
        logger.info("Command Sent: " + str(self.sendEncodedCommand))
        
        try:
            self.ser.write(self.sendEncodedCommand)
            logger.info("write data: " + str(self.sendEncodedCommand))
            #time.sleep(1)  #give the serial port sometime to receive the data
            serial_response = self.ser.readline(40)
            serial_response.decode("ascii")
            logger.info("Serial Response Is: " + str(serial_response))
            return serial_response.decode('ascii')
        except Exception as ex:
            logger.error("Failed to send data " + str(ex) + " " + str(self.ser))
            serial_response = ("error open serial port here: ")
            return (serial_response)
        
if __name__ == "__main__":
    logger.info("in main radio.py")
