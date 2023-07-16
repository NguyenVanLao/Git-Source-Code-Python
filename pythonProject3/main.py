import cv2
import numpy as np
import serial
from time import sleep
import serial.tools.list_ports
from tkinter import *
from PIL import ImageTk, Image
def get_ports():
    ports = serial.tools.list_ports.comports()
return ports
def findArduino(portsFound):
    commPort = 'None'
n   umConnection = len(portsFound)
for i in range(0, numConnection):
port = foundPorts[i]