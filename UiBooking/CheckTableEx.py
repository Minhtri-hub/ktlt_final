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
        time_str = self.comboBoxTime.currentText()

        seat_type = ""
        if self.radioButtonCounterSeating.isChecked():
            seat_type = "counter"
        elif self.radioButtonPrivateSeating.isChecked():
            seat_type = "private"
        else:
            QMessageBox.warning(self, "Error", "Table type not selected!")
            return

        json_file = "../dataset/checktable_data.json"
        # Ensure the path and file exist
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

        all_ids = []
        for seat_date, seat_obj in data.items():
            for seat_type_list in seat_obj.values():
                all_ids.extend(item.get("id", 0) for item in seat_type_list if isinstance(item, dict))

        next_global_id = max(all_ids, default=0) + 1

        if date_str not in data:
            data[date_str] = {"counter": [], "private": []}

        current_list = data[date_str][seat_type]
        max_capacity = 10 if seat_type == "counter" else 20

        if len(current_list) >= max_capacity:
            QMessageBox.information(self, "Notification", "All tables are full, please choose another date!")
            return


        new_item = {
            "id": next_global_id,
            "time": time_str,
            "people": people
        }
        current_list.append(new_item)

        try:
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Notification",
                                    "Table available! Switching to the Booking page.")
            self.open_booking_information()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unable to save data: {e}")

    def open_booking_information(self):
        self.booking_window = BookingInformationEx()
        self.booking_window.show()
        self.close()
