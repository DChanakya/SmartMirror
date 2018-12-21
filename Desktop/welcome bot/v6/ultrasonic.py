
import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 18
      PIN_ECHO = 24

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print("Waiting for sensor to settle")
      count = 0
      time.sleep(2)
      while 1:
          print("Calculating distance")

          GPIO.output(PIN_TRIGGER, GPIO.HIGH)

          time.sleep(0.00001)

          GPIO.output(PIN_TRIGGER, GPIO.LOW)

          while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
          while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

          pulse_duration = pulse_end_time - pulse_start_time
          distance = round(pulse_duration * 17150, 2)
          print("Distance:",distance,"cm")
          time.sleep(1)
          if(distance>33 and distance<120):
                count = count + 1
                if(count>2):
                      print('person is detected')
                      break;

finally:
      GPIO.cleanup()

