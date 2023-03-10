from gpiozero import Button

button = Button(3)

while True:
	if button.is_pressed:
		print("Boton presionado")
	else:
		print("Boton no presionado")
