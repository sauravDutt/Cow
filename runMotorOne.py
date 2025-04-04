from time import sleep
import RPi.GPIO as GPIO


DIR = 20  #DIRECTION GPIO Pin
STEP = 21 
CW = 1
CCW = 0
SPR = 48

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)