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
        people = int(self.comboBoxPeople.currentText())  # Get number of people from comboBox
        date_str = self.dateEditDate.text()  # Get date as a string
        time_str = self.comboBoxTime.currentText()  # Get time from comboBox

        seat_type = ""
        if self.radioButtonCounterSeating.isChecked():
            seat_type = "counter"
        elif self.radioButtonPrivateSeating.isChecked():
            seat_type = "private"
        else:
            QMessageBox.warning(self, "Lỗi", "Chưa chọn loại bàn!")  # Show a warning if no seat type is selected
            return

        json_file = "../dataset/checktable_data.json"
        # Ensure the path and file exist
        os.makedirs(os.path.dirname(json_file), exist_ok=True)
        if not os.path.exists(json_file):
            # Initialize the JSON file with an empty dictionary if it doesn't exist
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

        # Read and load the existing JSON data
        with open(json_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, dict):  # Validate that the loaded data is a dictionary
                    data = {}
            except json.JSONDecodeError:
                data = {}

        # Calculate the globally next available ID
        all_ids = []
        for seat_date, seat_obj in data.items():
            for seat_type_list in seat_obj.values():  # Iterate over "counter" and "private" lists
                all_ids.extend(item.get("id", 0) for item in seat_type_list if isinstance(item, dict))

        next_global_id = max(all_ids, default=0) + 1  # Find the highest ID in `all_ids` list and increment by 1

        # Initialize the date in `data` if not already present
        if date_str not in data:
            data[date_str] = {"counter": [], "private": []}

        # Get the appropriate list for the selected seat type
        current_list = data[date_str][seat_type]
        max_capacity = 10 if seat_type == "counter" else 20  # Capacity depends on seat type

        # Check if the seating capacity has been reached
        if len(current_list) >= max_capacity:
            QMessageBox.information(self, "Thông báo",
                                    "Đã hết bàn, vui lòng chọn ngày khác!")  # Notify if no tables are available
            return

        # Create the new booking item
        new_item = {
            "id": next_global_id,  # Use globally incremented ID
            "time": time_str,  # Time of booking
            "people": people  # Number of people
        }
        current_list.append(new_item)  # Append the new booking to the list

        # Write the updated data back to the JSON file
        try:
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Thông báo",
                                    "Còn bàn! Chuyển sang trang Booking.")  # Inform the user that booking is successful
            self.open_booking_information()  # Transition to the booking information page
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể lưu dữ liệu: {e}")  # Show an error message if saving fails

    def open_booking_information(self):
        self.booking_window = BookingInformationEx()
        self.booking_window.show()
        self.close()
