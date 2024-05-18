#This file is run on boot

from machine import Pin, I2C
from time import sleep

from lib.ssd1306 import SSD1306_I2C

# Initialize I2C Bus
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

oled_width, oled_height = 64, 48
device_address = 0x3C

# Initialize OLED
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr= device_address)

oled.fill(0)
oled.show()

oled.text("Hello", 0, 0)
oled.text("World", 0, 8)
oled.show()