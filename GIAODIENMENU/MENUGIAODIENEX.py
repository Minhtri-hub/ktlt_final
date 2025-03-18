from PyQt6.QtWidgets import QMainWindow
from GIAODIENMENU.MENUGIAODIEN import Ui_MainWindow


class MENUGIAODIENEX(QMainWindow, Ui_MainWindow):  # Inherit from QMainWindow and Ui_MainWindow
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Apply the UI setup to this QMainWindow instance

    def showWindow(self):
        self.show()
