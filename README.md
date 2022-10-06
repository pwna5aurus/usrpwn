This is my attempt to create a (basic) frontend for running pre-generated Python scripts from GNURadio in an attempt to make a portable USRP setup

I built a small Raspberry Pi touch screen setup and the screen is dinky and it's really hard to navigate with fingers so I wanted a UI that was basically just push-button, with some parameter fields that could be customized and passed as args to GNURadio scripts.  

I also wanted it to be 
1) Easy to maintain
2) OS agnostic

Ideally, this works best with a USRP SDR (I am using the B210), since the HackRF already has the Portapack for portability.  You could run it from your Mac or Windows laptop as well if you were so inclined (although I suppose that's not quite a fun).


To build a USRPwn you will need:
Raspberry Pi (4 recommended)
Portable battery to power everything (I bought the PST-MP3500-I from Powerstream)
USRP B210
USRP drivers
GNURadio
Python 3
Kivy (and probably a shitload of other depdendencies)


Some of that stuff isn't cheap, so it's not really "hobbyist-grade" materials, although this is very much a "hobbyist grade" project.


Will upload some pictures of this when it's closer to done.
