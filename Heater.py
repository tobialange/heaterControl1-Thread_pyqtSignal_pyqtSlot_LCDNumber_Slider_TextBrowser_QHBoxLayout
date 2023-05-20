from PyQt6.QtWidgets import QWidget, QTextBrowser
from PyQt6.QtCore import pyqtSlot
from PyQt6 import uic


class Heater(QWidget):
    textOffice = pyqtSlot(int)
    textLiving = pyqtSlot(int)
    textKitchen = pyqtSlot(int)

    def __init__(self, parent=None):
        super(Heater, self).__init__(parent)

        uic.loadUi("heater.ui", self)

        self.textBrowserOffice = self.findChild(QTextBrowser, "textBrowserOffice")
        self.textBrowserLiving = self.findChild(QTextBrowser, "textBrowserLiving")
        self.textBrowserKitchen = self.findChild(QTextBrowser, "textBrowserKitchen")

    def textOffice(self, soll):
        text = str(soll) + " °C"

        self.textBrowserOffice.setText(text)

    def textLiving(self, soll):
        text = str(soll) + " °C"

        self.textBrowserLiving.setText(text)

    def textKitchen(self, soll):
        text = str(soll) + " °C"

        self.textBrowserKitchen.setText(text)
