#!/usr/bin/python

import RPi.GPIO as gpio
import time

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(22, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)

def forward(sec):
 init()
 gpio.output(22, True)
 gpio.output(17, False)
 gpio.output(23, True)
 gpio.output(24, False)
 time.sleep(sec)

 gpio.output(22, gpio.LOW)
 gpio.output(17, gpio.LOW)
 gpio.output(23, gpio.LOW)
 gpio.output(24, gpio.LOW)
 
def reverse(sec):
 init()
 gpio.output(22, False)
 gpio.output(17, True)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(sec)
 
 gpio.output(22, gpio.LOW)
 gpio.output(17, gpio.LOW)
 gpio.output(23, gpio.LOW)
 gpio.output(24, gpio.LOW)

def right(sec):
 init()
 gpio.output(22, True)
 gpio.output(17, True)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(sec)
 
 gpio.output(22, gpio.LOW)
 gpio.output(17, gpio.LOW)
 gpio.output(23, gpio.LOW)
 gpio.output(24, gpio.LOW)


def left(sec):
 init()
 gpio.output(22, True)
 gpio.output(17, False)
 gpio.output(23, True)
 gpio.output(24, True)
 time.sleep(sec)

 gpio.output(22, gpio.LOW)
 gpio.output(17, gpio.LOW)
 gpio.output(23, gpio.LOW)
 gpio.output(24, gpio.LOW)


print "f = forward | b = back; | r = right | l = left |e = exit;"


motor_run = True
while(motor_run == True):
 x=raw_input()
 if x == 'f':
  print "forward"
  forward(.25)
  x='z'
 if x == 'b':
  print "back"
  reverse(.25)
 if x == 'r':
  print "right"
  right(.25)
 if x == 'l':
  print "left"
  left(.25)
 if ((x != 'f') or (x != 'b') or (x != 'e') or (x !='r') or (x != 'l')):
  print "Use f/b/r/l/e only!"
 if x == 'e':
  print "stopping"
  gpio.cleanup()
  time.sleep(.5)
  exit()


gpio.cleanup()
