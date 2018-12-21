import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BOARD)




IO.setup(3,IO.OUT) #GPIO 4 -> Motor 1 terminal A

IO.setup(5,IO.OUT) #GPIO 17 -> Motor Left terminal A
##IO.setup(6,IO.OUT) #GPIO 18 -> Motor Left terminal B
IO.setup(7,IO.OUT) #Left Motor Enabler
######IO.setup(8,IO.OUT) #Right Motor Enabler


##IO.setup(9,IO.OUT) #GPIO 2 -> Left IR out
##IO.setup(10,IO.OUT) #GPIO 3 -> Right IR out
IO.setup(11,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(12,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(13,IO.OUT) #GPIO 17 -> Motor Left terminal A
##IO.setup(14,IO.OUT) #GPIO 18 -> Motor Left terminal B
IO.setup(15,IO.OUT) #Left Motor Enabler
IO.setup(16,IO.OUT) #Right Motor Enabler


##IO.setup(17,IO.OUT) #GPIO 2 -> Left IR out
IO.setup(18,IO.OUT) #GPIO 3 -> Right IR out
IO.setup(19,IO.OUT) #GPIO 4 -> Motor 1 terminal A
##IO.setup(20,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(21,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(22,IO.OUT) #GPIO 18 -> Motor Left terminal B
IO.setup(23,IO.OUT) #Left Motor Enabler
IO.setup(24,IO.OUT) #Right Motor Enabler


##IO.setup(25,IO.OUT) #GPIO 2 -> Left IR out
IO.setup(26,IO.OUT) #GPIO 3 -> Right IR out
##IO.setup(27,IO.OUT) #GPIO 4 -> Motor 1 terminal A
##IO.setup(28,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(29,IO.OUT) #GPIO 17 -> Motor Left terminal A
##IO.setup(30,IO.OUT) #GPIO 18 -> Motor Left terminal B
IO.setup(31,IO.OUT) #Left Motor Enabler
IO.setup(32,IO.OUT) #Right Motor Enabler

IO.setup(33,IO.OUT) #GPIO 2 -> Left IR out
##IO.setup(34,IO.OUT) #GPIO 3 -> Right IR out
IO.setup(35,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(36,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(37,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(38,IO.OUT) #GPIO 18 -> Motor Left terminal B
##IO.setup(39,IO.OUT) #Left Motor Enabler
IO.setup(40,IO.OUT) #Right Motor Enabler
print('1')

IO.setup(3,IO.HIGH) #GPIO 4 -> Motor 1 terminal A

IO.setup(5,IO.HIGH) #GPIO 17 -> Motor Left terminal A
##IO.setup(6,IO.HIGH) #GPIO 18 -> Motor Left terminal B
IO.setup(7,IO.HIGH) #Left Motor Enabler
######IO.setup(8,IO.HIGH) #Right Motor Enabler


##IO.setup(9,IO.HIGH) #GPIO 2 -> Left IR HIGH
##IO.setup(10,IO.OUT) #GPIO 3 -> Right IR out
IO.setup(11,IO.HIGH) #GPIO 4 -> Motor 1 terminal A
IO.setup(12,IO.HIGH) #GPIO 14 -> Motor 1 terminal B
IO.setup(13,IO.HIGH) #GPIO 17 -> Motor Left terminal A
##IO.setup(14,IO.OUT) #GPIO 18 -> Motor Left terminal B
IO.setup(15,IO.HIGH) #Left Motor Enabler
IO.setup(16,IO.HIGH) #Right Motor Enabler


##IO.setup(17,IO.OUT) #GPIO 2 -> Left IR out
IO.setup(18,IO.HIGH) #GPIO 3 -> Right IR out
IO.setup(19,IO.HIGH) #GPIO 4 -> Motor 1 terminal A
##IO.setup(20,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(21,IO.HIGH) #GPIO 17 -> Motor Left terminal A
IO.setup(22,IO.HIGH) #GPIO 18 -> Motor Left terminal B
IO.setup(23,IO.HIGH) #Left Motor Enabler
IO.setup(24,IO.HIGH) #Right Motor Enabler


##IO.setup(25,IO.HIGH) #GPIO 2 -> Left IR out
IO.setup(26,IO.HIGH) #GPIO 3 -> Right IR out
##IO.setup(27,IO.HIGH) #GPIO 4 -> Motor 1 terminal A
##IO.setup(28,IO.HIGH) #GPIO 14 -> Motor 1 terminal B
IO.setup(29,IO.HIGH) #GPIO 17 -> Motor Left terminal A
##IO.setup(30,IO.OUT) #GPIO 18 -> Motor Left terminal B
IO.setup(31,IO.HIGH) #Left Motor Enabler
IO.setup(32,IO.HIGH) #Right Motor Enabler

IO.setup(33,IO.HIGH) #GPIO 2 -> Left IR out
##IO.setup(34,IO.OUT) #GPIO 3 -> Right IR out
IO.setup(35,IO.HIGH) #GPIO 4 -> Motor 1 terminal A
IO.setup(36,IO.HIGH) #GPIO 14 -> Motor 1 terminal B
IO.setup(37,IO.HIGH) #GPIO 17 -> Motor Left terminal A
IO.setup(38,IO.HIGH) #GPIO 18 -> Motor Left terminal B
##IO.setup(39,IO.OUT) #Left Motor Enabler
IO.setup(40,IO.OUT) #Right Motor Enabler

IO.cleanup()


