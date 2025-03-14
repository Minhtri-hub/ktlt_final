import os
import json
from PyQt6.QtWidgets import (
    QMainWindow, QTableWidgetItem, QMessageBox
)
from PyQt6.QtCore import pyqtSlot
from uiManagement.Management import Ui_MainWindow


class ManagementEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidgetEmployee.cellClicked.connect(self.on_employee_selected)
        self.tableWidgetBooking.cellClicked.connect(self.on_booking_selected)
        self.pushButtonCreateEmployee.clicked.connect(self.create_employee)
        self.pushButtonUpdateEmployee.clicked.connect(self.update_employee)
        self.pushButtonDeleteEmployee.clicked.connect(self.delete_employee)
        self.pushButtonCreateBooking.clicked.connect(self.create_booking)
        self.pushButtonUpdateBooking.clicked.connect(self.update_booking)
        self.pushButtonDeleteBooking.clicked.connect(self.delete_booking)
        self.load_employee_data()
        self.load_booking_data()

    def showWindow(self):
        self.show()

    def load_employee_data(self):
        self.tableWidgetEmployee.setRowCount(0)
        path = "../dataset/employee_data.json"
        if not os.path.exists(path):
            return
        with open(path, "r", encoding="utf-8") as f:
            try:
                employees = json.load(f)
            except:
                employees = []
        self.tableWidgetEmployee.setColumnCount(6)
        self.tableWidgetEmployee.setHorizontalHeaderLabels([
            "ID", "Name", "Username", "Password", "Hire Date", "Salary"
        ])
        self.tableWidgetEmployee.setRowCount(len(employees))
        for row, emp in enumerate(employees):
            e_id = str(emp.get("id", ""))
            e_name = emp.get("name", "")
            e_user = emp.get("username", "")
            e_pass = emp.get("password", "")
            e_hire = emp.get("hire_date", "")
            e_sal = str(emp.get("salary", ""))
            self.tableWidgetEmployee.setItem(row, 0, QTableWidgetItem(e_id))
            self.tableWidgetEmployee.setItem(row, 1, QTableWidgetItem(e_name))
            self.tableWidgetEmployee.setItem(row, 2, QTableWidgetItem(e_user))
            self.tableWidgetEmployee.setItem(row, 3, QTableWidgetItem(e_pass))
            self.tableWidgetEmployee.setItem(row, 4, QTableWidgetItem(e_hire))
            self.tableWidgetEmployee.setItem(row, 5, QTableWidgetItem(e_sal))

    def load_booking_data(self):
        self.tableWidgetBooking.setRowCount(0)  # Clear existing rows
        path = "../dataset/merged_data.json"  # Path to the merged JSON file

        # Check if the file exists
        if not os.path.exists(path):
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                merged_data = json.load(f)  # Load the JSON content
            except:
                merged_data = {}  # In case there's an issue with file contents

        # Prepare the table
        self.tableWidgetBooking.setColumnCount(8)  # Set up for 8 columns
        self.tableWidgetBooking.setHorizontalHeaderLabels([
            "Booking ID", "Full Name", "Email", "Mobile",
            "Seat Type", "Booking Date", "Total Customers", "Special Note"
        ])

        # List to hold rows (each row corresponds to booking information)
        all_bookings = []

        for date, bookings in merged_data.items():
            # Process 'private' bookings (if they exist)
            private_bookings = bookings.get("private", [])
            for booking in private_bookings:
                # Extract details from the `private` entry
                b_id = str(booking.get("id", ""))
                first_name = booking.get("first_name", "")
                last_name = booking.get("last_name", "")
                full_name = f"{first_name} {last_name}".strip()  # Combine names
                email = booking.get("email", "")
                mobile = booking.get("mobile", "")
                seat_type = booking.get("source", "")  # Use 'source' to infer seat type
                booking_time = booking.get("time", "")
                total_customers = str(booking.get("people", ""))
                special_note = booking.get("special_note", "")

                # Append the booking row
                all_bookings.append([
                    b_id, full_name, email, mobile, booking_time,
                    seat_type, date, total_customers, special_note
                ])

        # Populate the table widget
        self.tableWidgetBooking.setRowCount(len(all_bookings))  # Set number of rows
        for row, booking in enumerate(all_bookings):
            for col, value in enumerate(booking):
                self.tableWidgetBooking.setItem(row, col, QTableWidgetItem(value))

    @pyqtSlot(int, int)
    def on_employee_selected(self, row, col):
        e_id = self.tableWidgetEmployee.item(row, 0).text()
        e_name = self.tableWidgetEmployee.item(row, 1).text()
        e_user = self.tableWidgetEmployee.item(row, 2).text()
        e_pass = self.tableWidgetEmployee.item(row, 3).text()
        e_hire = self.tableWidgetEmployee.item(row, 4).text()
        e_sal = self.tableWidgetEmployee.item(row, 5).text()

        # Đẩy vào các line edit
        self.lineEditEmployeeID.setText(e_id)
        self.lineEditEmployeeName.setText(e_name)
        self.lineEditEmployeeUserName.setText(e_user)
        self.lineEditEmployeePass.setText(e_pass)
        self.lineEditEmployeeHireDate.setText(e_hire)
        self.lineEditEmployeeSalary.setText(e_sal)



    @pyqtSlot(int, int)
    def on_booking_selected(self, row, col):
        b_id = self.tableWidgetBooking.item(row, 0).text()
        b_name = self.tableWidgetBooking.item(row, 1).text()
        b_email = self.tableWidgetBooking.item(row, 2).text()
        b_mobile = self.tableWidgetBooking.item(row, 3).text()
        b_seat = self.tableWidgetBooking.item(row, 4).text()
        b_time = self.tableWidgetBooking.item(row, 5).text()
        b_cust = self.tableWidgetBooking.item(row, 6).text()
        b_note = self.tableWidgetBooking.item(row, 7).text()

        self.lineEditBookingID.setText(b_id)
        self.lineEditFullName.setText(b_name)
        self.lineEditEmail.setText(b_email)
        self.lineEditMobile.setText(b_mobile)
        self.comboBoxSeatType.setCurrentText(b_seat)
        self.lineEditBookingTime.setText(b_time)
        self.lineEditTotalCustomers.setText(b_cust)
        self.lineEditNote.setText(b_note)

    def create_employee(self):
        e_id = self.lineEditEmployeeID.text().strip()  # Employee ID
        e_name = self.lineEditEmployeeName.text().strip()  # Employee Name
        e_user = self.lineEditEmployeeUserName.text().strip()  # Username
        e_pass = self.lineEditEmployeePass.text().strip()  # Password
        e_hire = self.lineEditEmployeeHireDate.text().strip()  # Hire Date
        e_sal = self.lineEditEmployeeSalary.text().strip()  # Salary

        if not e_id or not e_name:  # Validate required fields
            QMessageBox.warning(self, "Error", "Employee ID và Name không được để trống!")
            return

        try:
            e_id = int(e_id)  # Ensure ID is an integer
            e_sal = int(e_sal)  # Ensure salary is a valid number
        except ValueError:
            QMessageBox.warning(self, "Error", "Employee ID và Salary phải là số nguyên!")
            return

        path = "../dataset/employee_data.json"
        if os.path.exists(path):  # Check if JSON exists
            with open(path, "r", encoding="utf-8") as f:
                try:
                    employees = json.load(f)
                except:
                    employees = []
        else:
            employees = []

        # Check if ID is already in use
        if any(int(emp.get("EmployeeId")) == e_id for emp in employees):
            QMessageBox.warning(self, "Error", f"Employee ID: {e_id} đã tồn tại!")
            return

        # Create new employee JSON entry
        new_emp = {
            "EmployeeId": e_id,
            "EmployeeName": e_name,
            "EmployeeUsername": e_user,
            "EmployeePass": e_pass,
            "hire_date": e_hire,
            "working_years": 0,  # Default working years to 0
            "salary": e_sal
        }

        employees.append(new_emp)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(employees, f, indent=4, ensure_ascii=False)

        QMessageBox.information(self, "Success", "Tạo nhân viên thành công!")
        self.load_employee_data()  # Reload employee table

    def update_employee(self):
        e_id = self.lineEditEmployeeID.text().strip()

        if not e_id:
            QMessageBox.warning(self, "Error", "Vui lòng nhập Employee ID để cập nhật!")
            return

        path = "employee_data.json"
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", "Không tìm thấy dữ liệu employee_data.json!")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                employees = json.load(f)
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Error", "Dữ liệu trong file không hợp lệ!")
                return

        updated = False
        for emp in employees:
            if emp.get("id") == e_id:
                emp["name"] = self.lineEditEmployeeName.text().strip()
                emp["username"] = self.lineEditEmployeeUserName.text().strip()
                emp["password"] = self.lineEditEmployeePass.text().strip()
                emp["hire_date"] = self.lineEditEmployeeHireDate.text().strip()
                emp["salary"] = self.lineEditEmployeeSalary.text().strip()
                updated = True
                break

        if updated:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(employees, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Success", "Cập nhật nhân viên thành công!")
            self.load_employee_data()  # Tải lại dữ liệu lên bảng
        else:
            QMessageBox.warning(self, "Error", f"Không tìm thấy Employee ID: {e_id}")

    def delete_employee(self):
        e_id = self.lineEditEmployeeID.text().strip()

        if not e_id:
            QMessageBox.warning(self, "Error", "Vui lòng nhập Employee ID để xóa!")
            return

        path = "employee_data.json"
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", "Không tìm thấy dữ liệu employee_data.json!")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                employees = json.load(f)
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Error", "Dữ liệu trong file không hợp lệ!")
                return

        original_length = len(employees)
        employees = [emp for emp in employees if emp.get("id") != e_id]

        if len(employees) < original_length:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(employees, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Success", "Xóa thành công nhân viên!")
            self.load_employee_data()  # Tải lại dữ liệu lên bảng
        else:
            QMessageBox.warning(self, "Error", f"Không tìm thấy Employee ID: {e_id}")

    def create_booking(self):
        b_id = self.lineEditBookingID.text().strip()  # Booking ID
        b_name = self.lineEditFullName.text().strip()  # Full Name
        b_email = self.lineEditEmail.text().strip()  # Email
        b_mobile = self.lineEditMobile.text().strip()  # Mobile
        b_seat = self.comboBoxSeatType.currentText()  # Seat Type
        b_time = self.lineEditBookingTime.text().strip()  # Booking Time
        b_cust = self.lineEditTotalCustomers.text().strip()  # Total Customers
        b_note = self.lineEditNote.text().strip()  # Special Note

        if not b_id or not b_name:  # Validate required fields
            QMessageBox.warning(self, "Error", "Booking ID và Full Name không được để trống!")
            return

        try:
            b_id = int(b_id)  # Ensure ID is an integer
            b_cust = int(b_cust) if b_cust else 0  # Ensure customers count is integer, default to 0
        except ValueError:
            QMessageBox.warning(self, "Error", "Booking ID và Total Customers phải là số nguyên!")
            return

        path = "../dataset/merged_data.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    bookings = json.load(f)
                except:
                    bookings = []
        else:
            bookings = []

        # Check if ID is already used
        if any(int(book.get("id")) == b_id for book in bookings):
            QMessageBox.warning(self, "Error", f"Booking ID: {b_id} đã tồn tại!")
            return

        # Create new booking JSON entry
        new_book = {
            "id": b_id,
            "full_name": b_name,
            "email": b_email,
            "mobile": b_mobile,
            "seat_type": b_seat,
            "booking_time": b_time,
            "total_customers": b_cust,
            "special_note": b_note
        }

        bookings.append(new_book)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(bookings, f, indent=4, ensure_ascii=False)

        QMessageBox.information(self, "Success", "Tạo booking thành công!")
        self.load_booking_data()  # Reload booking table

    def update_booking(self):
        b_id = self.lineEditBookingID.text().strip()

        if not b_id:
            QMessageBox.warning(self, "Error", "Vui lòng nhập Booking ID để cập nhật!")
            return

        path = "booking_data.json"
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", "Không tìm thấy dữ liệu booking_data.json!")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                bookings = json.load(f)
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Error", "Dữ liệu trong file không hợp lệ!")
                return

        updated = False
        for book in bookings:
            if book.get("id") == b_id:
                book["full_name"] = self.lineEditFullName.text().strip()
                book["email"] = self.lineEditEmail.text().strip()
                book["mobile"] = self.lineEditMobile.text().strip()
                book["seat_type"] = self.comboBoxSeatType.currentText().strip()
                book["booking_time"] = self.lineEditBookingTime.text().strip()
                book["total_customers"] = self.lineEditTotalCustomers.text().strip()
                book["special_note"] = self.lineEditNote.text().strip()
                updated = True
                break

        if updated:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(bookings, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Success", "Cập nhật booking thành công!")
            self.load_booking_data()
        else:
            QMessageBox.warning(self, "Error", f"Không tìm thấy Booking ID: {b_id}")

    def delete_booking(self):
        b_id = self.lineEditBookingID.text().strip()

        if not b_id:
            QMessageBox.warning(self, "Error", "Vui lòng nhập Booking ID để xóa!")
            return

        path = "booking_data.json"
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", "Không tìm thấy dữ liệu booking_data.json!")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                bookings = json.load(f)
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Error", "Dữ liệu trong file không hợp lệ!")
                return

        original_length = len(bookings)
        bookings = [book for book in bookings if book.get("id") != b_id]

        if len(bookings) < original_length:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(bookings, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Success", "Xóa thành công Booking!")
            self.load_booking_data()
        else:
            QMessageBox.warning(self, "Error", f"Không tìm thấy Booking ID: {b_id}")

