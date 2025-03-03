from PyQt6.QtWidgets import QMainWindow
from UiBooking.BookingInformation import Ui_BookingInformation

class BookingInformationEx(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BookingInformation()
        self.ui.setupUi(self)

    def showWindow(self):
        self.show()
