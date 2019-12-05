#!/bin/sh
clear
cat /opt/Final_Project/banner.txt
echo "Facial Recogniton Initiated"
python3 FinalFaceRecog.py
echo "Facial Recognition Passed"
sleep 2s
echo "RFID Verification Initiated"
python3 readRFID.py
echo "RFID Verification Passed"
sleep 2s
echo "Voice Activated Commands Ready; Front, Back, Exit"
python sopare.py -l
