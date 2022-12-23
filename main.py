import FakeRPi.GPIO as GPIO
from time import sleep

transistorPin = 17
currPos = 1
totalPatterns = 9
buttonWait = 0.021943

GPIO.setmode(GPIO.BCM)
GPIO.setup(transistorPin,GPIO.OUT)

def _simPress():
    GPIO.output(transistorPin, GPIO.HIGH)
    sleep(buttonWait)
    GPIO.output(transistorPin, GPIO.LOW)
    sleep(buttonWait)

def cycleTo(desiredPos):
    if desiredPos < currPos:
        presses = totalPatterns - currPos
        presses += desiredPos
    else:
        presses = desiredPos - currPos

    for _ in range(presses):
        _simPress()


cycleTo(9)
GPIO.cleanup()
