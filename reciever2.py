from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
import radio
message = radio.receive()
radio.config(group=5)
radio.on()
while True:
    if message == 'The area is safe there is no suspicious movement':
        display.show(Image.SAD)
        pin0.write_digital(1)        

    elif message == 'The area is safe there is no suspicious movement':
        display.show(Image.Happy)
        pin0.write_digital(0)
        