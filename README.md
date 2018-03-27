# AR8000
AOR AR8000 Wideband receiver control interface.

The AR8000 covers radio frequencies between 500KHz to 1900MHz without gaps.

This code provides serial conectivity to the AR8000 under Python3.5 and PyQt5 via linux with a simple physical serial interface.

You may have to insert the serial device:

find vendor and product numbers via 'lsusb'

Then inset similar to below:

"sudo modprobe usbserial vendor=0x067b product=0x2303"

Add user to dialout group:

"sudo usermod -a -G dialout $USER"

I will expand the explanation out, this insertion just works for me.

Provies GUI interface to control the radio function set.

Virtual enviroment via pipenv.

Just starting out, very early but it does read, write and control the radio.

What is working:
1) Serial connectivity via USB serial convertor.
2) Move up/down frequency with hard coded step size, soon to be definable via GUI.
3) Level Monitor.
4) Select band, NFM, WFM, AM, USB, LSB, CW, AU.
5) Mute on/off.
6) Start of the database of interesting frequencies.
