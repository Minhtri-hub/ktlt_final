from PyQt6.QtWidgets import QMainWindow, QMessageBox
from UiBooking.BookingInformation import Ui_BookingInformation
import json
import os
from datetime import datetime


class BookingInformationEx(QMainWindow, Ui_BookingInformation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonBookingTable.clicked.connect(self.handle_booking)

    def handle_booking(self):
        # Input data from the booking form
        first_name = self.lineEditFirstName.text().strip()
        last_name = self.lineEditLastName.text().strip()
        email = self.lineEditEmail.text().strip()
        mobile = self.lineEditMobile.text().strip()
        special_note = self.lineEditSpecialNote.text().strip()

        # Set default date and time if not provided (using current date and time)
        current_datetime = datetime.now()
        selected_date = current_datetime.strftime("%d/%m/%Y")  # Format: "01/11/2023" (day, month, year)
        selected_time = current_datetime.strftime("%I:%M %p")  # Format: "02:30 PM" (12-hour clock)

        # File paths
        booking_file_path = "../dataset/booking_data.json"
        os.makedirs(os.path.dirname(booking_file_path), exist_ok=True)

        # Read the existing booking data (if any) from JSON
        book_list = []
        if os.path.exists(booking_file_path):
            with open(booking_file_path, "r", encoding="utf-8") as f:
                try:
                    book_list = json.load(f)
                    if not isinstance(book_list, list):
                        book_list = []
                except json.JSONDecodeError:
                    book_list = []

        # Add a new booking entry and include date and time
        new_booking = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "mobile": mobile,
            "special_note": special_note,
            "date": selected_date,  # Save the date
            "time": selected_time  # Save the time
        }
        book_list.append(new_booking)

        # Save back to booking_data.json
        with open(booking_file_path, "w", encoding="utf-8") as json_file:
            json.dump(book_list, json_file, indent=4, ensure_ascii=False)

        # Notify the user of successful booking
        QMessageBox.information(self, 'Thông báo', 'Đăng ký thành công!')
        QMessageBox.information(self, 'Thông báo', f'Đã lưu thành công.\nNgày: {selected_date}, Giờ: {selected_time}')
        self.close()
