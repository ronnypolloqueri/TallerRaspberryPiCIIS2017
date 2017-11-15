import RPi.GPIO as GPIO
import sys

def inicializarBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
def definirPinoSalida(numeroPino):
    GPIO.setup(numeroPino, GPIO.OUT)
#    GPIO.output(numeroPino, estadoPuerto)
    
def escribirPuerto(numeroPino,estadoPuerto):
    GPIO.output(numeroPino,estadoPuerto)
