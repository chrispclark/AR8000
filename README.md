# AR8000
AOR AR8000 Wideband receiver control interface.

The AR8000 covers radio frequencies between 500KHz to 1900MHz without gaps.

This code provides serial conectivity to the AR8000 under Python3.5 and PyQt5 via linux with a simple physical serial interface via a usb to serial converter

Virtual enviroment via pipenv.

Just starting out, very early but it does read, write and control the radio.
The command set contains 80 functions of which only 5 are coded at this time.

What is working:
1) Serial connectivity via USB serial convertor.
2) GUI interface to the AR8000 command set.
3) Move up/down frequency.
4) Step size hard coded step size, soon to be definable via GUI.
5) Level Monitor.
6) Select band, NFM, WFM, AM, USB, LSB, CW, AU.
7) Mute on/off.
8) Start of the database of interesting frequencies.
