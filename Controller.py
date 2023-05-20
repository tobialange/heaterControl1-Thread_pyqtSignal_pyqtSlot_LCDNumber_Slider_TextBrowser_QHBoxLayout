from PyQt6.QtWidgets import QWidget, QLCDNumber, QSlider
from PyQt6.QtCore import pyqtSlot, pyqtSignal
from PyQt6 import uic


class Controller(QWidget):
    valueOffice = pyqtSlot(int)
    valueKitchen = pyqtSlot(int)
    valueLiving = pyqtSlot(int)

    changedTempOffice = pyqtSignal(int)
    changedTempKitchen = pyqtSignal(int)
    changedTempLiving = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Controller, self).__init__(parent)

        uic.loadUi("controller.ui", self)

        self.lcdNumberOffice = self.findChild(QLCDNumber, "lcdNumbeOffice")
        self.lcdNumberLiving = self.findChild(QLCDNumber, "lcdNumberLiving")
        self.lcdNumberKitchen = self.findChild(QLCDNumber, "lcdNumberKitchen")

        self.verticalSliderOffice = self.findChild(QSlider, "verticalSliderOffice")
        self.verticalSliderLiving = self.findChild(QSlider, "verticalSliderLiving")
        self.verticalSliderKitchen = self.findChild(QSlider, "verticalSliderKitchen")

        self.verticalSliderOffice.valueChanged.connect(self.valueOffice)
        self.verticalSliderKitchen.valueChanged.connect(self.valueKitchen)
        self.verticalSliderLiving.valueChanged.connect(self.valueLiving)

    def valueOffice(self, soll):
        self.changedTempOffice.emit(soll)

    def valueLiving(self, soll):
        self.changedTempLiving.emit(soll)

    def valueKitchen(self, soll):
        self.changedTempKitchen.emit(soll)
