import json
import os
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from uiManagement.BookingManagement import Ui_MainWindow

class BookingManagementEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bookings = []
        self.selected_row = None
        self.setupSignalAndSlot()
        self.load_booking_data()

    def showWindow(self):
        self.show()

    def setupSignalAndSlot(self):
        self.tableWidgetBookingList.itemClicked.connect(self.booking_selected)
        self.pushButtonClear.clicked.connect(self.clear_form)
        self.pushButtonSaveNew.clicked.connect(self.save_new_booking)
        self.pushButtonsaveUpdate.clicked.connect(self.update_booking)
        self.pushButtonDelete.clicked.connect(self.delete_booking)

    def load_booking_data(self):
        json_file_path = "dataset/booking_data.json"
        if not os.path.exists(json_file_path):
            return
        with open(json_file_path, "r", encoding="utf-8") as f:
            try:
                data_list = json.load(f)
                if not isinstance(data_list, list):
                    data_list = []
            except:
                data_list = []
        self.bookings = data_list
        self.refresh_table()

    def refresh_table(self):
        self.tableWidgetBookingList.setRowCount(0)
        for row, booking in enumerate(self.bookings):
            self.tableWidgetBookingList.insertRow(row)
            booking_id = str(booking.get("booking_id", ""))
            customer_id = str(booking.get("customer_id", ""))
            first_name = booking.get("first_name", "")
            last_name = booking.get("last_name", "")
            people = str(booking.get("people", ""))
            date_ = booking.get("date", "")
            time_ = booking.get("time", "")
            table_id = booking.get("table_id", "")
            seating_type = booking.get("seating_type", "")
            status = booking.get("status", "")
            self.tableWidgetBookingList.setItem(row, 0, QTableWidgetItem(booking_id))
            self.tableWidgetBookingList.setItem(row, 1, QTableWidgetItem(customer_id))
            self.tableWidgetBookingList.setItem(row, 2, QTableWidgetItem(f"{first_name} {last_name}".strip()))
            self.tableWidgetBookingList.setItem(row, 3, QTableWidgetItem(people))
            self.tableWidgetBookingList.setItem(row, 4, QTableWidgetItem(date_))
            self.tableWidgetBookingList.setItem(row, 5, QTableWidgetItem(time_))
            self.tableWidgetBookingList.setItem(row, 6, QTableWidgetItem(table_id))
            self.tableWidgetBookingList.setItem(row, 7, QTableWidgetItem(seating_type))
            self.tableWidgetBookingList.setItem(row, 8, QTableWidgetItem(status))

    def booking_selected(self, item):
        self.selected_row = item.row()
        self.lineEditBookingID.setText(self.tableWidgetBookingList.item(self.selected_row, 0).text())
        self.lineEditCustomerID.setText(self.tableWidgetBookingList.item(self.selected_row, 1).text())
        full_name = self.tableWidgetBookingList.item(self.selected_row, 2).text().split(maxsplit=1)
        self.lineEditFirstName.setText(full_name[0])
        if len(full_name) > 1:
            self.lineEditLastName.setText(full_name[1])
        else:
            self.lineEditLastName.clear()
        self.lineEditPeople.setText(self.tableWidgetBookingList.item(self.selected_row, 3).text())
        self.lineEditDate.setText(self.tableWidgetBookingList.item(self.selected_row, 4).text())
        self.lineEditTime.setText(self.tableWidgetBookingList.item(self.selected_row, 5).text())
        self.comboBoxSeatingType.setCurrentText(self.tableWidgetBookingList.item(self.selected_row, 7).text())
        self.comboBoxStatus.setCurrentText(self.tableWidgetBookingList.item(self.selected_row, 8).text())

    def save_new_booking(self):
        booking_id = self.lineEditBookingID.text().strip()
        customer_id = self.lineEditCustomerID.text().strip()
        first_name = self.lineEditFirstName.text().strip()
        last_name = self.lineEditLastName.text().strip()
        people = self.lineEditPeople.text().strip()
        date_ = self.lineEditDate.text().strip()
        time_ = self.lineEditTime.text().strip()
        table_id = ""
        seating_type = self.comboBoxSeatingType.currentText()
        status = self.comboBoxStatus.currentText()
        if not all([booking_id, customer_id, first_name, people, date_, time_]):
            QMessageBox.warning(self, "Error", "Please fill required fields!")
            return
        new_booking = {
            "booking_id": booking_id,
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "people": people,
            "date": date_,
            "time": time_,
            "table_id": table_id,
            "seating_type": seating_type,
            "status": status
        }
        self.bookings.append(new_booking)
        self.save_to_json()
        QMessageBox.information(self, "Success", "New booking saved!")
        self.refresh_table()
        self.clear_form()

    def update_booking(self):
        if self.selected_row is None:
            QMessageBox.warning(self, "Error", "No booking selected to update!")
            return
        booking_id = self.lineEditBookingID.text().strip()
        customer_id = self.lineEditCustomerID.text().strip()
        first_name = self.lineEditFirstName.text().strip()
        last_name = self.lineEditLastName.text().strip()
        people = self.lineEditPeople.text().strip()
        date_ = self.lineEditDate.text().strip()
        time_ = self.lineEditTime.text().strip()
        table_id = ""
        seating_type = self.comboBoxSeatingType.currentText()
        status = self.comboBoxStatus.currentText()
        if not all([booking_id, customer_id, first_name, people, date_, time_]):
            QMessageBox.warning(self, "Error", "Please fill required fields!")
            return
        self.bookings[self.selected_row] = {
            "booking_id": booking_id,
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "people": people,
            "date": date_,
            "time": time_,
            "table_id": table_id,
            "seating_type": seating_type,
            "status": status
        }
        self.save_to_json()
        QMessageBox.information(self, "Success", "Booking updated!")
        self.refresh_table()
        self.clear_form()

    def delete_booking(self):
        if self.selected_row is None:
            QMessageBox.warning(self, "Error", "No booking selected to delete!")
            return
        confirm = QMessageBox.question(self, "Confirm Delete", "Do you really want to delete this booking?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.bookings.pop(self.selected_row)
            self.save_to_json()
            QMessageBox.information(self, "Success", "Booking deleted!")
            self.refresh_table()
            self.clear_form()

    def clear_form(self):
        self.lineEditBookingID.clear()
        self.lineEditCustomerID.clear()
        self.lineEditFirstName.clear()
        self.lineEditLastName.clear()
        self.lineEditPeople.clear()
        self.lineEditDate.clear()
        self.lineEditTime.clear()
        self.comboBoxSeatingType.setCurrentIndex(0)
        self.comboBoxStatus.setCurrentIndex(0)
        self.lineEditSpecial.clear()
        self.lineEditEmail.clear()
        self.lineEditMobile.clear()
        self.selected_row = None

    def save_to_json(self):
        json_file_path = "dataset/booking_data.json"
        os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
        with open(json_file_path, "w", encoding="utf-8") as f:
            json.dump(self.bookings, f, indent=4, ensure_ascii=False)
