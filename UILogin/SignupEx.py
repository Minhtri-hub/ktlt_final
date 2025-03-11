from UILogin.Signup import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox
import os
import json

class SignupEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonBack.clicked.connect(self.back_to_login)
        self.pushButtonSignUp.clicked.connect(self.handle_signup)

    def back_to_login(self):
        self.MainWindow.close()
        from UILogin.LoginCustomerEx import LoginCustomerEx
        from PyQt6.QtWidgets import QMainWindow
        self.login_window = QMainWindow()
        self.login_ui = LoginCustomerEx()
        self.login_ui.setupUi(self.login_window)
        self.login_window.show()

    def handle_signup(self):
        username = self.lineEditUsername.text().strip()
        password = self.lineEditPass.text().strip()
        email = self.lineEditEmail.text().strip()
        phone = self.lineEditPhoneNumber.text().strip()
        name = self.lineEditYourName.text().strip()

        json_file_path = "../dataset/customer_data.json"
        os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

        data_list = []
        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as f:
                try:
                    data_list = json.load(f)
                    if not isinstance(data_list, list):
                        data_list = []
                except json.JSONDecodeError:
                    data_list = []

        max_id = 0
        for user in data_list:
            uid = user.get("id", 0)
            if uid > max_id:
                max_id = uid

        new_id = max_id + 1

        new_user = {
            "id": new_id,
            "username": username,
            "password": password,
            "email": email,
            "phone_number": phone,
            "name": name
        }

        data_list.append(new_user)

        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)

        QMessageBox.information(self.MainWindow, 'Thông báo', 'Đăng ký thành công!')
        QMessageBox.information(self.MainWindow, 'Thông báo', 'Đã lưu thành công, vui lòng đăng nhập lại')

        self.MainWindow.close()
