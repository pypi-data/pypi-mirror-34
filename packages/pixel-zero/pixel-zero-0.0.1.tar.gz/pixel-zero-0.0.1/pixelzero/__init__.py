"""
  _____ _          _ ______              
 |  __ (_)        | |___  /              
 | |__) |__  _____| |  / / ___ _ __ ___  
 |  ___/ \ \/ / _ \ | / / / _ \ '__/ _ \ 
 | |   | |>  <  __/ |/ /_|  __/ | | (_) |
 |_|   |_/_/\_\___|_/_____\___|_|  \___/ 
The easy to use library for Neopixels on Pi

==============================================
PixelZero is a port of Damien George's MicroPython Neopixel library.
==============================================
AGPL-3.0 License
"""
import os

user = os.getenv("SUDO_USER")
if user is None:
    print("Please run Python as root, neopixels don't work when not run as root :)")
    exit()

from neopixel import *

class NeoPixel:
    ORDER = (1, 0, 2, 3)
    
    def __init__(self, pin, n, bpp=3, timing=0):
        global strip
        self.pin = pin
        self.n = n
        self.bpp = bpp
        self.buf = bytearray(n * bpp)
        self.timing = timing
        strip = Adafruit_NeoPixel(n, pin) 
        global allpix
        allpix = self.n
        strip.begin()
    
     
    def __setitem__(self, index, val):
        sone = str(val)
        stwo = sone.replace("(", "")
        sthree = stwo.replace(")", "")
        data = sthree.split(", ")
        r = int(data[0])
        g = int(data[1])
        b = int(data[2])

        strip.setPixelColorRGB(index, r, g, b)
    
    def show(self):
        strip.show()
    
    def clear(self):
        strip.setPixelColorRGB(n, 0, 0, 0)
        strip.show()
