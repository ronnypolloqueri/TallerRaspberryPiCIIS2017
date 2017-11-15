import RPi.GPIO as GPIO # importa biblioteca GPIO
import time 		# importa biblioteca de temporizacion

GPIO.setmode(GPIO.BOARD) #GPIO / usando numeracion fisica
GPIO.setwarnings(False)  # desahabilitar los mensajes

GPIO.setup(7, GPIO.OUT) # pine 23 definido como salida

while(1):
    print('LED ON')

    GPIO.output(7, GPIO.HIGH) # enciende LED
    time.sleep(2)		   # retardo de segundos
    print('LED OFF')	   # mensaje LED OFF
    GPIO.output(7, GPIO.LOW)  # apaga LED
    time.sleep(2)

