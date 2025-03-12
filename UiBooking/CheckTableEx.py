import json
import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from UiBooking.CheckTable import Ui_MainWindow
from UiBooking.BookingInformationEx import BookingInformationEx

class CheckTableEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonCheckAvailability.clicked.connect(self.handle_check_availability)

    def handle_check_availability(self):
        people = int(self.comboBoxPeople.currentText())
        date_str = self.dateEditDate.text()
        time_str = self.comboBoxTime.currentText()  # Lấy time từ comboBox

        seat_type = ""
        if self.radioButtonCounterSeating.isChecked():
            seat_type = "counter"
        elif self.radioButtonPrivateSeating.isChecked():
            seat_type = "private"
        else:
            QMessageBox.warning(self, "Lỗi", "Chưa chọn loại bàn!")
            return

        json_file = "../dataset/checktable_data.json"
        os.makedirs(os.path.dirname(json_file), exist_ok=True)
        if not os.path.exists(json_file):
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

        with open(json_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
            except json.JSONDecodeError:
                data = {}

        if date_str not in data:
            data[date_str] = {"counter": [], "private": []}

        current_list = data[date_str][seat_type]
        max_capacity = 10 if seat_type == "counter" else 20

        if len(current_list) >= max_capacity:
            QMessageBox.information(self, "Thông báo", "Đã hết bàn, vui lòng chọn ngày khác!")
            return

        new_item = {
            "time": time_str,
            "people": people
        }
        current_list.append(new_item)

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        QMessageBox.information(self, "Thông báo", "Còn bàn! Chuyển sang trang Booking.")
        self.open_booking_information()

    def open_booking_information(self):
        self.booking_window = BookingInformationEx()
        self.booking_window.show()
        self.close()
