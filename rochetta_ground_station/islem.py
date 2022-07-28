from PyQt6.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
import imutils
import cv2
import serial
from serial import Serial

try:
    ser = serial.Serial("COM5", 9600)
except:
    ser = "52"


def rotate_image_by_angle(image, angle):
    # Rotate the image by the given angle.
    return imutils.rotate(image, angle=angle)

class Worker(QObject):
    finished = pyqtSignal()
    photoReady = pyqtSignal(str)
    photo_path = "src/rochetta.png"
    image = cv2.imread(r"{}".format(photo_path))


    @pyqtSlot()
    def photo_updater(self):
        while True:
            try:
                gelen = ser.readline()
                gelen = gelen.decode()
            except:
                #gelen = "52"
                gelen = 0
            for i in range(0,180,1):
                gelen = str(i)
                new_photo = rotate_image_by_angle(self.image, 360 - int(gelen))
                cv2.imwrite("src/rotated_image.png", new_photo)
                stri = "src/rotated_image.png?{}".format(gelen)
                time.sleep(0.08)
                self.photoReady.emit(stri)
            for i in range(180,0,-1):
                gelen = str(i)
                new_photo = rotate_image_by_angle(self.image, 360 - int(gelen))
                cv2.imwrite("src/rotated_image.png", new_photo)
                stri = "src/rotated_image.png?{}".format(gelen)
                time.sleep(0.08)
                self.photoReady.emit(stri)
            self.finished.emit()
