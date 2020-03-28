import RPi.GPIO as GPIO
import time


def drive(direction):
    if direction == 'FORWARD':
        forward()
    elif direction == 'REVERSE':
        reverse()
    elif direction == 'LEFT':
        left()
    elif direction == 'RIGHT':
        right()
    else:
        brake()


def cleanup():
    GPIO.cleanup()


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)


def forward():
    init()
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def reverse():
    init()
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)


def brake():
    init()
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)


def left():
    init()
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def right():
    init()
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
