from PyQt6.QtWidgets import QMainWindow
from UiBooking.CheckTable import Ui_MainWindow
from UiBooking.BookingInformationEx import BookingInformationEx

class CheckTableEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()

    def showWindow(self):
        self.show()

    def setupSignalAndSlot(self):
        self.pushButtonCheckAvailability.clicked.connect(self.openBookingInformation)

    def openBookingInformation(self):
        self.booking_window = BookingInformationEx()
        self.booking_window.showWindow()
        self.close()
