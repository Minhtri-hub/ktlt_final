from UILogin.Login import Ui_MainWindow
from UiBooking.CheckTableEx import CheckTableEx
from data.Import_data_from_json import get_data_from_json
from PyQt6.QtWidgets import QMessageBox

class LoginCustomerEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = None
        self.customers = get_data_from_json("customer_data.json")

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        if not self.customers:
            QMessageBox.critical(self.MainWindow,"Lỗi","Không có dữ liệu khách hàng. Kiểm tra file customer_data.json!")
            return
        self.setupSignalAndSlot()
        self.checkboxisChecked()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.handle_login)
        self.checkBox.stateChanged.connect(self.checkboxisChecked)
        self.pushButtonSignUp.clicked.connect(self.handle_signup)

    def checkboxisChecked(self):
        self.pushButtonLogin.setEnabled(self.checkBox.isChecked())

    def handle_login(self):
            username = self.lineEditUsername.text().strip()
            password = self.lineEditPassword.text().strip()
            if not self.customers:
                QMessageBox.warning(self.MainWindow,"Lỗi","Không có dữ liệu khách hàng!")
                return
            user = None
            for customer in self.customers:
                if customer.get("username") == username and customer.get("password") == password:
                    user = customer
                    break
            if user:
                QMessageBox.information(self.MainWindow,"Thành công",f"Đăng nhập thành công! Chào mừng {user.get('name')}")
                print(f"Đăng nhập thành công! Chào mừng {user.get('name')}")
                self.checktable = CheckTableEx()
                self.checktable.show()
                self.MainWindow.close()
            else:
                QMessageBox.warning(self.MainWindow,"Lỗi","Tên đăng nhập hoặc mật khẩu không đúng!")

    def handle_signup(self):
        from UILogin.SignupEx import SignupEx
        from PyQt6.QtWidgets import QMainWindow
        self.signup_window = QMainWindow()
        self.signup_ui = SignupEx()
        self.signup_ui.setupUi(self.signup_window)
        self.signup_window.show()
        self.MainWindow.close()
