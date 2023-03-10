from gpiozero import LED
from signal import pause

red=LED(3) #pin logico
red.blink()
pause()
