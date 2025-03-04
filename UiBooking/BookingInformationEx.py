from PyQt6.QtWidgets import QMainWindow, QMessageBox
from UiBooking.BookingInformation import Ui_BookingInformation
import json
import os

class BookingInformationEx(QMainWindow, Ui_BookingInformation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonBookingTable.clicked.connect(self.handle_booking)

    def handle_booking(self):
        first_name = self.lineEditFirstName.text().strip()
        last_name = self.lineEditLastName.text().strip()
        email = self.lineEditEmail.text().strip()
        mobile = self.lineEditMobile.text().strip()
        special_note = self.lineEditSpecialNote.text().strip()

        json_file_path = "../dataset/booking_data.json"
        os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

        book_list = []
        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as f:
                try:
                    book_list = json.load(f)
                    if not isinstance(book_list, list):
                        book_list = []
                except json.JSONDecodeError:
                    book_list = []

        new_booking = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "mobile": mobile,
            "special_note": special_note
        }

        book_list.append(new_booking)

        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(book_list, json_file, indent=4, ensure_ascii=False)

        QMessageBox.information(self, 'Thông báo', 'Đăng ký thành công!')
        QMessageBox.information(self, 'Thông báo', 'Đã lưu thành công, vui lòng đăng nhập lại')
        self.close()
