from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from uiManagement.BookingManagement import Ui_MainWindow
from model.Booking import Booking
import datetime

class BookingManagementExt(Ui_MainWindow):
    def __init__(self, data_connector):
        super().__init__()
        self.data_connector = data_connector
        self.selected_booking = None

    def setupUi(self, window):
        super().setupUi(window)
        self.window = window
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        self.tableWidgetBookingList.itemClicked.connect(self.booking_selected)
        self.pushButtonSaveNew.clicked.connect(self.save_new_booking)
        self.pushButtonsaveUpdate.clicked.connect(self.update_booking)
        self.pushButtonDelete.clicked.connect(self.delete_booking)
        self.pushButtonClear.clicked.connect(self.clear_form)

        # Load dữ liệu booking
        self.load_booking_table()

    def load_booking_table(self):
        """Load dữ liệu booking từ DataConnector và hiển thị lên QTableWidget"""
        self.tableWidgetBookingList.setRowCount(0)  # Xóa bảng cũ
        bookings = self.data_connector.load_bookings()

        for row, booking in enumerate(bookings):
            self.tableWidgetBookingList.insertRow(row)
            self.tableWidgetBookingList.setItem(row, 0, QTableWidgetItem(booking.booking_id))
            self.tableWidgetBookingList.setItem(row, 1, QTableWidgetItem(booking.customer_id))
            self.tableWidgetBookingList.setItem(row, 2, QTableWidgetItem(f"{booking.first_name} {booking.last_name}"))
            self.tableWidgetBookingList.setItem(row, 3, QTableWidgetItem(str(booking.people)))
            self.tableWidgetBookingList.setItem(row, 4, QTableWidgetItem(booking.date))
            self.tableWidgetBookingList.setItem(row, 5, QTableWidgetItem(booking.time))
            self.tableWidgetBookingList.setItem(row, 6, QTableWidgetItem(booking.seating_type))
            self.tableWidgetBookingList.setItem(row, 7, QTableWidgetItem(booking.status))

    def booking_selected(self, item):
        """Khi click vào một booking, điền thông tin vào form"""
        row = item.row()
        self.selected_booking = self.tableWidgetBookingList.item(row, 0).text()

        self.lineEditBookingID.setText(self.tableWidgetBookingList.item(row, 0).text())
        self.lineEditCustomerID.setText(self.tableWidgetBookingList.item(row, 1).text())
        full_name = self.tableWidgetBookingList.item(row, 2).text().split()
        self.lineEditFirstName.setText(full_name[0])
        self.lineEditLastName.setText(full_name[1] if len(full_name) > 1 else "")
        self.lineEditPeople.setText(self.tableWidgetBookingList.item(row, 3).text())
        self.dateEditDate.setDate(datetime.datetime.strptime(self.tableWidgetBookingList.item(row, 4).text(), "%Y-%m-%d").date())
        self.comboBoxTime.setCurrentText(datetime.datetime.strptime(self.tableWidgetBookingList.item(row, 5).text(), "%H:%M").strftime("%H:%M"))
        self.comboBoxSeatingType.setCurrentText(self.tableWidgetBookingList.item(row, 6).text())
        self.comboBoxStatus.setCurrentText(self.tableWidgetBookingList.item(row, 7).text())

    def save_new_booking(self):
        """Lưu đơn đặt bàn mới"""
        booking = Booking(
            booking_id=self.lineEditBookingID.text(),
            customer_id=self.lineEditCustomerID.text(),
            first_name=self.lineEditFirstName.text(),
            last_name=self.lineEditLastName.text(),
            email=self.lineEditEmail.text(),
            mobile=self.lineEditMobile.text(),
            people=self.lineEditPeople.text().strip(),
            date=self.dateEditDate.text(),
            time=self.comboBoxTime.currentText(),
            seating_type=self.comboBoxSeatingType.currentText(),
            status=self.comboBoxStatus.currentText(),
            special_note=self.lineEditSpecial.text()
        )

        bookings = self.data_connector.load_bookings()
        bookings.append(booking)
        if self.data_connector.save_bookings(bookings):
            QMessageBox.information(self.window, "Success", "Booking saved successfully!")
            self.load_booking_table()
            self.clear_form()
        else:
            QMessageBox.warning(self.window, "Error", "Failed to save booking.")

    def update_booking(self):
        """Cập nhật đơn đặt bàn"""
        if not self.selected_booking:
            QMessageBox.warning(self.window, "Error", "Please select a booking to update!")
            return

        bookings = self.data_connector.load_bookings()
        for booking in bookings:
            if booking.booking_id == self.selected_booking:
                booking.first_name = self.lineEditFirstName.text()
                booking.last_name = self.lineEditLastName.text()
                booking.people = int(self.lineEditPeople.text())
                booking.date = self.dateEditDate.text()
                booking.time = self.comboBoxTime.currentText()
                booking.seating_type = self.comboBoxSeatingType.currentText()
                booking.status = self.comboBoxStatus.currentText()
                booking.special_note = self.lineEditSpecial.toPlainText()
                break

        if self.data_connector.save_bookings(bookings):
            QMessageBox.information(self.window, "Success", "Booking updated successfully!")
            self.load_booking_table()
        else:
            QMessageBox.warning(self.window, "Error", "Failed to update booking.")

    def delete_booking(self):
        """Xóa đơn đặt bàn với xác nhận từ người dùng"""

        # 🛑 Kiểm tra trước khi thực hiện xóa
        if not self.selected_booking:
            QMessageBox.warning(self.window, "Error", "Please select a booking to delete!")
            return

        # 🛑 Hiển thị hộp thoại xác nhận trước khi xóa
        msg = QMessageBox(self.window)
        msg.setText(f"Do you really want to delete booking [{self.selected_booking}]?")
        msg.setWindowTitle("Confirm Delete")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)

        # Nếu chọn "No" thì không xóa
        if msg.exec() == QMessageBox.StandardButton.No:
            return

        # 🗑️ Xóa booking được chọn
        bookings = self.data_connector.load_bookings()
        bookings = [b for b in bookings if b.booking_id != self.selected_booking]

        # 🔄 Cập nhật lại dữ liệu
        if self.data_connector.save_bookings(bookings):
            QMessageBox.information(self.window, "Success", "Booking deleted successfully!")

            # 🔄 Load lại danh sách booking sau khi xóa
            self.load_booking_table()
            self.clear_form()  # Xóa dữ liệu trên form sau khi xóa booking
            self.selected_booking = None  # Reset biến lưu booking đang chọn
        else:
            QMessageBox.warning(self.window, "Error", "Failed to delete booking.")

    def clear_form(self):
        """Xóa toàn bộ dữ liệu nhập trên form"""
        self.lineEditBookingID.clear()
        self.lineEditCustomerID.clear()
        self.lineEditFirstName.clear()
        self.lineEditLastName.clear()
        self.lineEditEmail.clear()
        self.lineEditMobile.clear()
        self.lineEditPeople.clear()
        self.lineEditSpecial.clear()

        # Đặt lại combobox về lựa chọn đầu tiên
        self.comboBoxSeatingType.setCurrentIndex(0)
        self.comboBoxStatus.setCurrentIndex(0)
        self.comboBoxTime.setCurrentIndex(0)
        self.comboBoxStatus.setCurrentIndex(0)
        self.dateEditDate.setCurrentSectionIndex(0)

        # Reset biến lưu booking đang chọn
        self.selected_booking = None