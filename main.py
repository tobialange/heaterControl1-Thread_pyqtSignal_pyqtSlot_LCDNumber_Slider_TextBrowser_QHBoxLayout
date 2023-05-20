import sys
from PyQt6 import QtWidgets
from MyMainWindow import MyMainWindow


app = QtWidgets.QApplication(sys.argv)
dialog = MyMainWindow()
dialog.show()
sys.exit(app.exec())