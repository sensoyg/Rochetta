from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt, QTimer, QThread
from PyQt6 import QtGui
from cv2 import transform
import imutils
import cv2
import sys
import islem



timer = QTimer()
class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.obj = islem.Worker()
        self.thread = QThread()
        self.obj.photoReady.connect(self.init_ui)
        self.obj.moveToThread(self.thread)
        self.obj.finished.connect(self.thread.quit)
        self.thread.started.connect(self.obj.photo_updater)
        self.thread.start()
        loadUi("src/main.ui", self)
        self.setWindowTitle("Rochetta Yer İstasyonu")
        self.setWindowIcon(QIcon("src/rochetta_temsili_resized.png"))
        self.show()



    def init_ui(self, stri):
        splitted = stri.split("?")
        pixmap = QPixmap(splitted[0])
        self.angle_label.setText(splitted[1].strip())
        self.label.setStyleSheet("background-color:white;")
        self.label.setPixmap(pixmap)

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())

