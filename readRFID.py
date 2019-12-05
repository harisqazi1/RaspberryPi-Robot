#!/usr/bin/python3
import time
import os
import signal
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
 
#signal.signal(signal.SIGINT, signal.SIG_IGN) #Meant to Disable CTRL + C 


Loop = True

print("Scan RFID")

reader = SimpleMFRC522()
id ,text = reader.read()

print(id) #Prints the id of the RFID Chip
print(text)  #Prints text stored on RFID Chip

x=0
while (Loop == True):
   if (id == 512149238788):  #This is the id of the Verified RFID Chip
      print("Verfified User")
      Loop = False  #Set the value of the loop to False, so then the loop can end
      GPIO.cleanup()  #Not needed for code to work, but recommended
   else:
      if (id != 512149238788):
         String = "Unauthorized User | [Info:] Try Number:number"
         print(String.replace("number", str(x)))
         x +=1
        


#os.kill(os.getppid(), signal.SIGHUP)  #SIGHUP tells the terminal to exit

