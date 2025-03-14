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
        self.tableWidgetEmployee.setRowCount(0)  # Clear the table
        path = "../dataset/employee_data.json"  # Path to the JSON file

        if not os.path.exists(path):  # Check if the file exists
            print(f"File not found: {path}")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                employees = json.load(f)  # Load the employee data
            except json.JSONDecodeError as e:
                print(f"Error loading JSON: {e}")
                employees = []

        # Set up table columns
        self.tableWidgetEmployee.setColumnCount(6)
        self.tableWidgetEmployee.setHorizontalHeaderLabels([
            "ID", "Name", "Username", "Password", "Hire Date", "Salary"
        ])

        # Populate the table
        self.tableWidgetEmployee.setRowCount(len(employees))  # Set row count
        for row, emp in enumerate(employees):
            e_id = str(emp.get("EmployeeId", ""))  # Corrected key for EmployeeId
            e_name = emp.get("EmployeeName", "")  # Corrected key for EmployeeName
            e_user = emp.get("EmployeeUsername", "")  # Corrected key for EmployeeUsername
            e_pass = emp.get("EmployeePass", "")  # Corrected key for EmployeePass
            e_hire = emp.get("hire_date", "")  # `"hire_date"` remains correct
            e_sal = str(emp.get("salary", ""))  # `"salary"` remains correct

            # Set table items
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
            print("Error: merged_data.json file does not exist")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                merged_data = json.load(f)  # Load the JSON content
            except json.JSONDecodeError:
                print("Error: Invalid JSON content in merged_data.json")
                return

        # Validate that the root structure is a list
        if not isinstance(merged_data, list):
            print("Error: Expected a list in merged_data.json, but received something else.")
            return

        # Prepare the table
        self.tableWidgetBooking.setColumnCount(9)  # Define 9 columns
        self.tableWidgetBooking.setHorizontalHeaderLabels([
            "Booking ID", "Full Name", "Email", "Mobile",
            "Seat Type", "Booking Time", "Total Customers", "Special Note", "Booking Date"
        ])

        # List to hold rows (each row corresponds to booking information)
        all_bookings = []

        # Iterate over the list and extract the necessary information
        for booking in merged_data:
            b_id = str(booking.get("id", ""))  # Booking ID
            first_name = booking.get("first_name", "")
            last_name = booking.get("last_name", "")
            full_name = f"{first_name} {last_name}".strip()  # Combine names safely
            email = booking.get("email", "")
            mobile = booking.get("mobile", "")
            seat_type = booking.get("seat_type", "")  # Seat type
            booking_time = booking.get("time", "")
            total_customers = str(booking.get("people", ""))  # Total customers
            special_note = booking.get("special_note", "")
            booking_date = booking.get("date", "")  # Booking date

            # Append the booking row to our list
            all_bookings.append([
                b_id, full_name, email, mobile,
                seat_type, booking_time, total_customers, special_note, booking_date
            ])

        # Populate the table widget with the bookings
        self.tableWidgetBooking.setRowCount(len(all_bookings))  # Set the row count based on data
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
        b_date = self.tableWidgetBooking.item(row, 8).text()  # Booking date (added)

        # Set values to the appropriate line edits/combobox
        self.lineEditBookingID.setText(b_id)
        self.lineEditFullName.setText(b_name)
        self.lineEditEmail.setText(b_email)
        self.lineEditMobile.setText(b_mobile)
        self.comboBoxSeatType.setCurrentText(b_seat)
        self.lineEditBookingTime.setText(b_time)
        self.lineEditTotalCustomers.setText(b_cust)
        self.lineEditNote.setText(b_note)
        self.lineEditBookingDate.setText(b_date)  # Set the booking date

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

        path = "../dataset/employee_data.json"
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
        e_id = self.lineEditEmployeeID.text().strip()  # Get Employee ID from the input

        if not e_id:
            QMessageBox.warning(self, "Error", "Vui lòng nhập Employee ID để xóa!")
            return

        path = "../dataset/employee_data.json"  # Path to the JSON file
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", "Không tìm thấy dữ liệu employee_data.json!")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                employees = json.load(f)  # Load employee data from the JSON file
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Error", "Dữ liệu trong file không hợp lệ!")
                return

        # Ensure comparison consistency between e_id and the JSON EmployeeId
        original_length = len(employees)

        # Check both integer and string possibilities for comparison
        employees = [emp for emp in employees if str(emp.get("EmployeeId", "")) != e_id]

        if len(employees) < original_length:  # If any employee was deleted
            with open(path, "w", encoding="utf-8") as f:
                json.dump(employees, f, indent=4, ensure_ascii=False)  # Save updated JSON
            QMessageBox.information(self, "Success", "Xóa thành công nhân viên!")
            self.load_employee_data()  # Reload employee table data
        else:
            QMessageBox.warning(self, "Error", f"Không tìm thấy Employee ID: {e_id}")

    def create_booking(self):
        b_id = self.lineEditBookingID.text().strip()
        b_name = self.lineEditFullName.text().strip()
        b_email = self.lineEditEmail.text().strip()
        b_mobile = self.lineEditMobile.text().strip()
        b_seat = self.comboBoxSeatType.currentText()
        b_time = self.lineEditBookingTime.text().strip()
        b_cust = self.lineEditTotalCustomers.text().strip()
        b_note = self.lineEditNote.text().strip()
        b_date = self.lineEditBookingDate.text().strip()

        if not b_id or not b_name or not b_date:
            QMessageBox.warning(self, "Error", "Booking ID, Full Name, và Booking Date không được để trống!")
            return

        try:
            b_id = int(b_id)
            b_cust = int(b_cust) if b_cust else 0
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

        if any(int(book.get("id", 0)) == b_id for book in bookings):
            QMessageBox.warning(self, "Error", f"Booking ID: {b_id} đã tồn tại!")
            return

        new_book = {
            "id": b_id,
            "full_name": b_name,
            "email": b_email,
            "mobile": b_mobile,
            "seat_type": b_seat,
            "booking_time": b_time,
            "total_customers": b_cust,
            "special_note": b_note,
            "date": b_date
        }

        bookings.append(new_book)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(bookings, f, indent=4, ensure_ascii=False)

        QMessageBox.information(self, "Success", "Tạo booking thành công!")
        self.load_booking_data()

    def update_booking(self):
        b_id = self.lineEditBookingID.text().strip()

        if not b_id:
            QMessageBox.warning(self, "Error", "Vui lòng nhập Booking ID để cập nhật!")
            return

        path = "../dataset/merged_data.json"  # Use merged_data.json
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", "Không tìm thấy dữ liệu merged_data.json!")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                bookings = json.load(f)  # Load the booking data
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Error", "Dữ liệu trong file không hợp lệ!")
                return

        # Update the entry with matching Booking ID
        updated = False
        for book in bookings:
            if str(book.get("id")) == b_id:  # Match Booking ID
                book["full_name"] = self.lineEditFullName.text().strip()
                book["email"] = self.lineEditEmail.text().strip()
                book["mobile"] = self.lineEditMobile.text().strip()
                book["seat_type"] = self.comboBoxSeatType.currentText().strip()
                book["booking_time"] = self.lineEditBookingTime.text().strip()
                book["total_customers"] = int(
                    self.lineEditTotalCustomers.text().strip()) if self.lineEditTotalCustomers.text().strip().isdigit() else 0
                book["special_note"] = self.lineEditNote.text().strip()
                book["date"] = self.lineEditBookingDate.text().strip()  # Add or update 'date' field
                updated = True
                break

        if updated:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(bookings, f, indent=4, ensure_ascii=False)  # Save changes to file
            QMessageBox.information(self, "Success", "Cập nhật booking thành công!")
            self.load_booking_data()  # Reload table data
        else:
            QMessageBox.warning(self, "Error", f"Không tìm thấy Booking ID: {b_id}")

    def delete_booking(self):
        b_id = self.lineEditBookingID.text().strip()  # Get the Booking ID from the input field

        if not b_id:
            QMessageBox.warning(self, "Error", "Vui lòng nhập Booking ID để xóa!")
            return

        path = "../dataset/merged_data.json"  # Use merged_data.json file
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", "Không tìm thấy dữ liệu merged_data.json!")
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                bookings = json.load(f)  # Load booking data from the file
            except json.JSONDecodeError:
                QMessageBox.warning(self, "Error", "Dữ liệu trong file không hợp lệ!")
                return

        # Track the original length of data and filter out the record with matching Booking ID
        original_length = len(bookings)
        bookings = [book for book in bookings if str(book.get("id")) != b_id]

        if len(bookings) < original_length:  # Check if any record was removed
            with open(path, "w", encoding="utf-8") as f:
                json.dump(bookings, f, indent=4, ensure_ascii=False)  # Save updated bookings to the file
            QMessageBox.information(self, "Success", "Xóa thành công Booking!")
            self.load_booking_data()  # Reload table data
        else:
            QMessageBox.warning(self, "Error", f"Không tìm thấy Booking ID: {b_id}")

