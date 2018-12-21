import RPi.GPIO as GPIO
import time
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(7,GPIO.HIGH)

def motor1():
    init()
    print('forward')
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(16,GPIO.LOW)
    time.sleep(1)
    stop()

def motor2():
    init()
    print('reverse')
    GPIO.output(18,GPIO.LOW)
    GPIO.output(16,GPIO.HIGH)
    time.sleep(0.9)
    stop()

def servo():
    init()
    print('hand shake')
    pwm=GPIO.PWM(11,50)
    pwm.start(5)
    i=1
    while i<=3:    
        pwm.ChangeDutyCycle(7)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(10)
        time.sleep(0.5)
        print(i)
        i=i+1
        pwm.ChangeDutyCycle(7)
        time.sleep(0.2)
    stop()

def stop():
    init()
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(16,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.cleanup()

motor1()
time.sleep(1.5)
servo()
time.sleep(1.5)
motor2()


