#reciever
from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
import radio 
radio.on()
radio.config(group=66)


while True:
    message=radio.receive()
    if message =="help,the temperature here is killing us":
        pin8.write_digital(1)
        pin0.write_digital(1)
     #   add_text(3,4, message)
        display.show('a')
    else:
        pin0.write_digital(0)
        pin8.write_digital(0)
    #    add_text(3,4,'The area is safe')