import RPi.GPIO as GPIO
import time

# AIN1
MOTORPIN1 = 12
# AIN2
MOTORPIN2 = 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTORPIN1, GPIO.OUT)
GPIO.setup(MOTORPIN2, GPIO.OUT)

ML11 = GPIO.PWM(MOTORPIN1, 100)
ML11.start(0)
ML12 = GPIO.PWM(MOTORPIN2, 100)
ML12.start(0)

while True:
    try:
        ML11.ChangeDutyCycle(10)
        ML12.ChangeDutyCycle(0)
        time.sleep(3)
        ML11.ChangeDutyCycle(20)
        ML12.ChangeDutyCycle(0)
        time.sleep(3)
        ML11.ChangeDutyCycle(0)
        ML12.ChangeDutyCycle(0)
        time.sleep(3)
        ML11.ChangeDutyCycle(0)
        ML12.ChangeDutyCycle(10)
        time.sleep(3)
        ML11.ChangeDutyCycle(0)
        ML12.ChangeDutyCycle(20)
        time.sleep(3)
    except KeyboardInterrupt:
        ML11.stop()
        ML12.stop()
        GPIO.cleanup()