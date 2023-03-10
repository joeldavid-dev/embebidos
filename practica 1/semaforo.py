from gpiozero import LED, Button
from time import sleep
from signal import pause

button=Button(17)
ledVerde = LED(2)
ledAmbar = LED(3)
ledRojo = LED(4)

def pasoPeatonal():
	ledVerde.off()
	ledAmbar.on()
	ledRojo.off()
	sleep(2)
	print("Led amarillo")
	ledAmbar.off()
	return True

def semaforo():
	ledRojo.on()
	if(button.is_pressed): return False
	sleep(3)
	ledRojo.off()
	if (button.is_pressed): return False
	ledVerde.on()
	if (button.is_pressed): return False
	sleep(3)
	if (button.is_pressed): return False
	ledVerde.off()
	if (button.is_pressed): return False
	ledAmbar.on()
	if (button.is_pressed): return False
	sleep(1)
	if (button.is_pressed): return False
	ledAmbar.off()
	if (button.is_pressed): return False
	ledRojo.on()
	if (button.is_pressed): return False
	sleep(3)
	if (button.is_pressed): return False
	ledRojo.off()
	if (button.is_pressed): return False
	return True
	
while True:
	condicion=True
	while (condicion == True):
		condicion = semaforo()
	condicion = pasoPeatonal()
	
