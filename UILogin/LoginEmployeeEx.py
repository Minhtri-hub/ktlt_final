from PyQt6.QtWidgets import QMessageBox
from UILogin.LoginEmployee import Ui_MainWindow
from data.Import_data_from_json import get_data_from_json
from uiManagement.ManagementEx import ManagementEx

class LoginEmployeeEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.employees = get_data_from_json("../dataset/employee_data.json")

    def setupSignalAndSlot(self):
        self.pushButtonLoginEmployee.clicked.connect(self.handle_login_employee)

    def handle_login_employee(self):
        username = self.lineEditUsernameEmployee.text().strip()
        password = self.lineEditPasswordEmployee.text().strip()

        if not self.employees:
            QMessageBox.warning(self.MainWindow, "Error", "No employee data!")
            return

        user = None
        for employee in self.employees:
            if employee.get("EmployeeUsername") == username and employee.get("EmployeePass") == password:
                user = employee
                break

        if user:
            QMessageBox.information(
                self.MainWindow,
                "Success",
                f"Login successful! Welcome {user.get('EmployeeName')}"
            )
            print(f"Login successful! Welcome {user.get('EmployeeName')}")

            self.booking_management = ManagementEx()
            self.booking_management.showWindow()

            self.MainWindow.close()
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")
