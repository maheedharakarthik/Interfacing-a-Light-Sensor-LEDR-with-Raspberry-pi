import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ldr_threshold = 1000
LDR_PIN = 18
LIGHT_PIN = 25

def readLDR (PIN):
  reading=0
  GPIO.setup(LIGHT_PIN, GPIO>OUT)
  GPIO.output(PIN,False)
  time.sleep(0.1)
  GPIO.setup(PIN, GPIO.IN)
  while (GPIO.input (PIN)==False):
    reading=reading+1
    return reading

def switchOnLight (PIN):
  GPIO.setup(PIN,GPIO.OUT)
  GPIO.output(PIN,True)

def swtichOffLight(PIN):
  GPIO.sestup(PIN, GPIO.OUT)
  GPIO.output(PIN, False)

while True:
  ldr_reading = readLDR(LDR_PIN)
  if ldr_reading < ldr_threshold:
    swtichOnLight (LIGHT_PIN)
  else:
    switchOffLight(LIGHT_PIN)

time.sleep(1)
