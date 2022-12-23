from time import sleep
from os import environ, path

if "PILIGHTS_DEV" in environ:
    import FakeRPi.GPIO as GPIO
else:
    import RPi.GPIO as GPIO


def _simPress(pin, wait):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    sleep(wait)
    GPIO.output(pin, GPIO.LOW)
    sleep(wait)
    GPIO.cleanup()


def _checkStatus():
    if path.isfile("./.lightpos"):
        with open(".lightpos", "r") as posfile:
            return int(posfile.readline())
    else:
        return 1


def _writeStatus(status):
    with open("./lightpos", "w+") as f:
        f.write(status)


def cycleTo(desiredpos):
    totalpatterns = 9
    transistorpin = 17
    buttonwait = 0.021943
    currpos = _checkStatus()
    if desiredpos < currpos:
        presses = totalpatterns - currpos
        presses += desiredpos
    else:
        presses = desiredpos - currpos
    for _ in range(presses):
        _simPress(transistorpin, buttonwait)


cycleTo(9)
