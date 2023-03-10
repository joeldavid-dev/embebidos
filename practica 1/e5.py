from gpiozero import Button

button = Button(17)

button.wait_for_press()
print("El boton fue presionado")