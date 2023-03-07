#
from microbit import *
import radio 
radio.on()
radio.config(group=66)


while True:
    temp=temperature()
    display.scroll(temp)
    
    if temp >= 20:
        radio.send("help,the temperature here is killing us")

        




