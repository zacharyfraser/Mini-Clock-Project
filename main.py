#This file is run on boot

from machine import Pin, I2C
import network
import math
import utime

import lib.ntptime as ntptime
from lib.ssd1306 import SSD1306_I2C

# Initialize I2C Bus
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Initialize Wifi
wifi = network.WLAN(network.STA_IF)

oled_width, oled_height = 64, 48
device_address = 0x3C

ssid = "BELL106"
password = "5D5CA234CE56"
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
     utime.sleep(1)
print("Connected to Wi-Fi")
print(f"IP Address: {wifi.ifconfig()[0]}")

# Initialize NTP
ntp_time = ntptime.settime()
print(f"Initialized NTP Time")

# Initialize OLED
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr= device_address)

time_format = "{:02}-{:02}"

while(True):
    current_time_UTC = utime.localtime()
    current_time_seconds = utime.mktime(current_time_UTC) - 3*3600 # type: ignore
    current_time_tuple = utime.localtime(current_time_seconds)
    current_time = time_format.format(current_time_tuple[3], current_time_tuple[4])
    oled.fill(0)
    oled.text(current_time, 12, 20, 1)
    oled.show()
    utime.sleep(1)