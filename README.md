# RaspberryPi-Robot
Purpose:

This is an Independent Study project I did. This is a robot that is run by a Raspberry Pi 3. The main outcome of this project is to do facial recogition, RFID scan, and after that is complete, move the robot through voice commands.

NOTE: All the code is NOT here. There are some code that are in folders, and since Github does not allow folders, I suggest following the links in Resources below to get what you want to fully work. The code I have provided worked with my project. 

Materials:
Raspberry Pi 3b,
Raspberry Pi Camera,
Portable Battery,
Microphone,
RFID Reader,
L298 Motor

Resources:

*These are the websites I used for the major parts of the project.*

https://www.hackster.io/bestd25/pi-car-016e66  (Building the Car)

https://raspberrypi.stackexchange.com/questions/100253/how-can-i-install-opencv-on-raspberry-pi-4-raspbian-buster (Downloading OpenCV for Facial Recognition)

https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826 (How to do Facial Recognition)

https://pimylifeup.com/raspberry-pi-rfid-rc522/ (RFID setup)

https://www.instructables.com/id/RFID-RC522-Raspberry-Pi/ (RFID setup)

http://www.piddlerintheroot.com/l298n-dual-h-bridge/ (Motor Setup)

https://github.com/opencv/opencv/tree/master/data/haarcascades (OpenCV Recognition code)

https://www.bishoph.org/step-by-step-raspberry-pi-offline-voice-recognition-with-sopare/ (Voice Recognition)



Code:


*I forgot what packages I installed to make the code work. If there is a problem, search online how to fix it.*


01_face_dataset.py - (Part 1 of the Facial Recognition) for training the face recognition software. Can be modified to take more pictures to train more precisely.

02_face_training.py - (Part 2 of the Facial Recognition) Trains the Program with the data from part 1.

More coming soon...
