import RPi.GPIO as GPIO
import sys

def inicializarBoard():
    GPIO.setmode(GPIO.BOARD) # utilizando la referencia de los pines
    GPIO.setwarnings(False)   # deshabilita los mensajes

def definePinoComoSalida(numeroPino):
    GPIO.setup(numeroPino, GPIO.OUT)
    GPIO.output(numeroPino, estadoPuerta)

def escribeParaPuerta(numeroPino,estadoPuerta):
    GPIO.output(numeroPino,estadoPuerta)

numeroPino = int(sys.argv[1]) # leer parametros
estadoPuerta = int(sys.argv[2])

inicializarBoard()
definePinoComoSalida(numeroPino)
escribeParaPuerta(numeroPino, estadoPuerta)
