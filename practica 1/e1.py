from gpiozero import LED
from time import sleep

red=LED(3) #pin logico

while True:
	red.on() #Se enciende el led
	sleep(1)#Espera
	red.off()#Sen apaga el led
	sleep(1)#Espera
