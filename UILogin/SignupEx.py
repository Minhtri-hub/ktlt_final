from UILogin.Signup import Ui_MainWindow
from data.Import_data_from_json import get_data_from_json
from PyQt6.QtWidgets import QMessageBox


class SignupEx(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.handle_signup()
        self.setupSignalAndSlot()
        self.checkboxisChecked()

    def __init__(self):
        self.customers = get_data_from_json("customer_data.json")
        if not self.customers:
            QMessageBox.critical(MainWindow, "Lỗi")
            exit(1)

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonSignUp.clicked.connect(self.handle_signup)
        self.pushButtonBack.clicked.connect(self.checkboxisChecked)
    def handle_signup(self):
        pass

    def checkboxisChecked(self):
        from UILogin.LoginCustomerEx import LoginCustomerEx

        def go_back_to_login(self):
            self.login_window = LoginCustomerEx()
            self.login_window.show()
            self.MainWindow.close()

