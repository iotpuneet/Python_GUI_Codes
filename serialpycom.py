import serial
import time

ser = serial.Serial('COM7', baudrate = 9600, timeout =1)

while 1:
    arduinoData = ser.readline().decode('ASCII')
    print(arduinoData)
    time.sleep(0.5)
