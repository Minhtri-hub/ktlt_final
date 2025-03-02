from UILogin.Login import Ui_MainWindow
from UiBooking.BookingInformationEx import BookingWindowEx
from data.Import_data_from_json import get_data_from_json
from PyQt6.QtWidgets import QMessageBox


class LoginCustomerEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.handle_login()
        self.setupSignalAndSlot()
        self.checkboxisChecked()


    def __init__(self):
        self.customers = get_data_from_json("customer_data.json")
        if not self.customers:
            QMessageBox.critical(MainWindow, "Lỗi", "Không có dữ liệu khách hàng. Kiểm tra file customer_data.json!")
            exit(1)

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.handle_login)
        self.checkBox.stateChanged.connect(self.checkboxisChecked)
        self.pushButtonSignUp.clicked.connect(self.signupisChecked)

    def showWindow(self):
        self.MainWindow.show()

    def checkboxisChecked(self):
        self.pushButtonLogin.setEnabled(self.checkBox.isChecked())

    def handle_login(self):
        username = self.lineEditUsername.text().strip()
        password = self.lineEditPassword.text().strip()

        if not getattr(self, "customers") or not self.customers:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không có dữ liệu khách hàng!")
            return

        user = None
        for customer in self.customers:
            if customer.get("username") == username and customer.get("password") == password:
                user = customer
                break  # Dừng vòng lặp khi tìm thấy user

        if user:
            QMessageBox.information(self.MainWindow, "Thành công",
                                    f"Đăng nhập thành công! Chào mừng {user.get('name')}")
            print(f"Đăng nhập thành công! Chào mừng {user.get('name')}")

            # Mở cửa sổ Booking
            self.booking_window = BookingWindowEx()
            self.booking_window.show()

            # Đóng cửa sổ đăng nhập
            self.MainWindow.close()
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def signupisChecked(self):

