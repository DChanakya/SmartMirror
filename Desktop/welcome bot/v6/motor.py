import RPi.GPIO as GPIO
import os
import time
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(29,GPIO.OUT)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.output(29,GPIO.HIGH)

def motor1():
    init()
    print('forward')
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(31,GPIO.LOW)
    time.sleep(1)
    stop()

def motor2():
    init()
    print('reverse')
    GPIO.output(33,GPIO.LOW)
    GPIO.output(31,GPIO.HIGH)
    time.sleep(1)
    stop()

def servo():
    init()
    print('hand shake')
    pwm=GPIO.PWM(37,50)
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
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(31,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.cleanup()
while(1):
    if( os.stat("buf1.txt").st_size > 0 ):
        f=open("buf1.txt","w")
        f.write("")
        f.close()
        break


motor1()
time.sleep(1.5)
servo()
time.sleep(1.5)
motor2()


