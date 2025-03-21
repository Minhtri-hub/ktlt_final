from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from GIAODIENMENU.MENUGIAODIENEX import MENUGIAODIENEX
from UiBooking.BookingInformation import Ui_BookingInformation
import json
from datetime import datetime
import os


class BookingInformationEx(QMainWindow, Ui_BookingInformation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()
        self.pushButtonBookingTable.setEnabled(False)

    def showWindow(self):
        self.show()

    def setupSignalAndSlot(self):
        self.checkBoxConfirmBooking.stateChanged.connect(self.isChecked)
        self.checkBoxReceiveMenu.stateChanged.connect(self.isChecked)
        self.pushButtonBookingTable_2.clicked.connect(self.handle_booking)
    def isChecked(self):
        if self.checkBoxConfirmBooking.isChecked():
            self.pushButtonBookingTable_2.setEnabled(True)
        else:
            self.pushButtonBookingTable_2.setEnabled(False)


    def handle_booking(self):

        if self.checkBoxReceiveMenu.isChecked():
            self.menu_dialog = MENUGIAODIENEX()
            self.menu_dialog.showWindow()

        full_name = self.lineEditFullName.text().strip()
        email = self.lineEditEmail.text().strip()
        mobile = self.lineEditMobile.text().strip()
        special_note = self.lineEditSpecialNote.text().strip()


        if not full_name or not email or not mobile:
            QMessageBox.warning(self, 'Error', 'Please enter all the required information.')
            return

        # Prepare the booking file path
        booking_file_path = "../dataset/booking_data.json"
        os.makedirs(os.path.dirname(booking_file_path), exist_ok=True)

        book_list = []
        max_id = 0
        if os.path.exists(booking_file_path):
            with open(booking_file_path, "r", encoding="utf-8") as f:
                try:
                    book_list = json.load(f)
                    if isinstance(book_list, list):
                        max_id = max((booking["id"] for booking in book_list if "id" in booking), default=0)
                    else:
                        book_list = []
                except json.JSONDecodeError:
                    book_list = []

        current_datetime = datetime.now()
        new_booking = {
            "id": max_id + 1,  # Increment the maximum ID
            "full_name": full_name,
            "email": email,
            "mobile": mobile,
            "special_note": special_note,
        }
        book_list.append(new_booking)

        # Save to `booking_data.json`
        with open(booking_file_path, "w", encoding="utf-8") as json_file:
            json.dump(book_list, json_file, indent=4, ensure_ascii=False)

        # Notify the user of successful booking
        QMessageBox.information(self, 'Notification', 'Registration successful!')
        QMessageBox.information(self, 'Notification',
                                f'Successfully booked on {current_datetime.strftime("%Y-%m-%d")} at {current_datetime.strftime("%H:%M:%S")}!')
        self.close()
