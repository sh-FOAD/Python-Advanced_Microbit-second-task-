from microbit import *
from ultrasonic import Ultrasonic
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
import radio
message = radio.receive()
radio.config(group=5)
radio.on()
ultra = Ultrasonic()

while True:
    initialize()
    clear_oled()
    distance = ultra.measure_distance_cm()
    add_text(1, 1, str(int(distance_value)))
    pir = pin2.read_digital()
    add_text(2, 2, str(int(pir)))
    
    if pir == 1:
        display.show(Image.SAD)
        pin0.write_digital(1)
        
        radio.send('Warning, there is a suspicious movment around',distance,pir)
        
    elif pir == 0:
        radio.send('The area is safe there is no suspicious movement')
        
    radio.send(distance,pir)