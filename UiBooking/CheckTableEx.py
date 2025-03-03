from PyQt6.QtWidgets import QMainWindow

from UiBooking.CheckTable import Ui_MainWindow # Import giao diện đặt bàn

class CheckTableEx(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def showWindow(self):
        self.MainWindow.show()