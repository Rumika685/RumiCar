import RPi.GPIO as GPIO
import time

# 一つ目のモータのピン
MOTORPIN1 = 12
# 二つ目のモータのピン
MOTORPIN2 = 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTORPIN1, GPIO.OUT)
GPIO.setup(MOTORPIN2, GPIO.OUT)

ML1 = GPIO.PWM(MOTORPIN1, 100)
ML1.start(0)
ML2 = GPIO.PWM(MOTORPIN2, 100)
ML2.start(0)

while True:
    try:
        ML1.ChangeDutyCycle(10)
        ML2.ChangeDutyCycle(0)
        time.sleep(3)
        ML1.ChangeDutyCycle(20)
        ML2.ChangeDutyCycle(0)
        time.sleep(3)
        ML1.ChangeDutyCycle(30)
        ML2.ChangeDutyCycle(0)
        time.sleep(3)
        ML1.ChangeDutyCycle(0)
        ML2.ChangeDutyCycle(10)
        time.sleep(3)
        ML1.ChangeDutyCycle(0)
        ML2.ChangeDutyCycle(20)
        time.sleep(3)
        ML1.ChangeDutyCycle(0)
        ML2.ChangeDutyCycle(30)
        time.sleep(3)
        ML1.ChangeDutyCycle(0)
        ML2.ChangeDutyCycle(0)
        time.sleep(3)
    except KeyboardInterrupt:
        ML1.stop()
        ML2.stop()
        GPIO.cleanup()

