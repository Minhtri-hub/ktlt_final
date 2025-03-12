
from uiManagement.BookingManagement import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow

class BookingManagementEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showWindow(self):
        self.show()
