from PyQt6.QtWidgets import QMainWindow, QMessageBox
from UiBooking.BookingInformation import Ui_BookingInformation
import json
from datetime import datetime
import os


class BookingInformationEx(QMainWindow, Ui_BookingInformation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()
        self.pushButtonBookingTable.setEnabled(False)  # Vô hiệu hóa nút ngay từ đầu

    def showWindow(self):
        self.show()

    def setupSignalAndSlot(self):
        self.checkBoxConfirmBooking.stateChanged.connect(self.isChecked)
        self.checkBoxReceiveMenu.stateChanged.connect(self.isChecked)
        self.pushButtonBookingTable.clicked.connect(self.handle_booking)
    def isChecked(self):
        if self.checkBoxConfirmBooking.isChecked():
            self.pushButtonBookingTable.setEnabled(True)


    def handle_booking(self):
        if self.checkBoxReceiveMenu.isChecked():
            pass
        full_name = self.lineEditFullName.text().strip()
        email = self.lineEditEmail.text().strip()
        mobile = self.lineEditMobile.text().strip()
        special_note = self.lineEditSpecialNote.text().strip()

        # Validate user inputs
        if not full_name or not email or not mobile:
            QMessageBox.warning(self, 'Lỗi', 'Vui lòng nhập đầy đủ thông tin cần thiết.')
            return

        # Prepare the booking file path
        booking_file_path = "../dataset/booking_data.json"
        os.makedirs(os.path.dirname(booking_file_path), exist_ok=True)

        book_list = []
        max_id = 0  # Track the maximum ID found
        if os.path.exists(booking_file_path):
            with open(booking_file_path, "r", encoding="utf-8") as f:
                try:
                    book_list = json.load(f)
                    if isinstance(book_list, list):
                        # Find the maximum existing ID in the booking list
                        max_id = max((booking["id"] for booking in book_list if "id" in booking), default=0)
                    else:
                        book_list = []
                except json.JSONDecodeError:
                    book_list = []

        # Create a new booking entry
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
        QMessageBox.information(self, 'Thông báo', 'Đăng ký thành công!')
        QMessageBox.information(self, 'Thông báo',
                                f'Đã đặt thành công vào ngày {current_datetime.strftime("%Y-%m-%d")} lúc {current_datetime.strftime("%H:%M:%S")}!')
        self.close()
