from gpiozero import LED, Button
from signal import pause

led = LED(2)
button = Button(17)

button.when_pressed = led.on
button.when_released = led.off

pause()