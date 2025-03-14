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
            # If the JSON file doesn't exist, initialize it with an empty dictionary
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

        # Read and load the data from the JSON file
        with open(json_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, dict):  # Ensure the structure is a dictionary
                    data = {}
            except json.JSONDecodeError:
                data = {}

        # Initialize the date in `data` if not already present
        if date_str not in data:
            data[date_str] = {"counter": [], "private": []}

        # Get the appropriate list for the selected seat_type
        current_list = data[date_str][seat_type]
        max_capacity = 10 if seat_type == "counter" else 20

        # Check if the seating capacity has been reached
        if len(current_list) >= max_capacity:
            QMessageBox.information(self, "Thông báo", "Đã hết bàn, vui lòng chọn ngày khác!")
            return

        # Calculate the next available ID
        next_id = 1  # Default ID if there are no existing bookings
        if current_list:
            next_id = max(item.get("id", 0) for item in current_list) + 1  # Increment from the highest existing ID

        # Create the new booking item
        new_item = {
            "id": next_id,
            "time": time_str,
            "people": people
        }
        current_list.append(new_item)  # Append the new booking to the list

        # Write the updated data back to the JSON file
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        QMessageBox.information(self, "Thông báo", "Còn bàn! Chuyển sang trang Booking.")
        self.open_booking_information()

    def open_booking_information(self):
        self.booking_window = BookingInformationEx()
        self.booking_window.show()
        self.close()
