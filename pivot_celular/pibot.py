import RPi.GPIO as GPIO				# importa bliblioteca GPIO
import time
import getch

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A_DERECHA = 16					# mapeamiento de los motores
A_IZQUIERDA = 11
R_DERECHA = 18
R_IZQUIERDA = 13

def setup_motor():				# setup de los motores
    GPIO.setup(A_DERECHA,GPIO.OUT)
    GPIO.setup(A_IZQUIERDA,GPIO.OUT)
    GPIO.setup(R_DERECHA,GPIO.OUT)
    GPIO.setup(R_IZQUIERDA,GPIO.OUT)

def mover_adelante():				# mover adelante
    GPIO.output(A_DERECHA,GPIO.HIGH)
    GPIO.output(A_IZQUIERDA,GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(A_DERECHA,GPIO.LOW)
    GPIO.output(A_IZQUIERDA,GPIO.LOW)

def mover_retro():				# mover marcha retro
    GPIO.output(R_DERECHA,GPIO.HIGH)
    GPIO.output(R_IZQUIERDA,GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(R_DERECHA,GPIO.LOW)
    GPIO.output(R_IZQUIERDA,GPIO.LOW)

def mover_derecha():				# mover derecha
    GPIO.output(A_IZQUIERDA,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(A_IZQUIERDA,GPIO.LOW)

def mover_izquierda():				# mover izquierda
    GPIO.output(A_DERECHA,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(A_DERECHA,GPIO.LOW)

def mover_parar():				# para todos los motores
    GPIO.output(A_DERECHA,GPIO.LOW)
    GPIO.output(A_IZQUIERDA,GPIO.LOW)
    GPIO.output(R_DERECHA,GPIO.LOW)
    GPIO.output(R_IZQUIERDA,GPIO.LOW)


