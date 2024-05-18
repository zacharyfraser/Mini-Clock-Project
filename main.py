#This file is run on boot

from machine import Pin, I2C
from time import sleep

from lib.ssd1306 import SSD1306_I2C

# Initialize I2C Bus
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

width, height = 64, 48
device_address = 0x3C

# Initialize OLED
oled = SSD1306_I2C(width, height, i2c, addr= device_address)

oled.fill(1)
oled.show()