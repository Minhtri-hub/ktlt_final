from UILogin.Login import Ui_MainWindow
from data.Import_data_from_json import get_data_from_json
from PyQt6.QtWidgets import QMessageBox


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Tải dữ liệu khách hàng từ file JSON và lưu vào thuộc tính
        self.customers = get_data_from_json("customer_data.json")
        if not self.customers:
            QMessageBox.critical(MainWindow, "Lỗi", "Không có dữ liệu khách hàng. Kiểm tra file customer_data.json!")
            exit(1)

        # Kết nối sự kiện nút đăng nhập (giả sử bạn có QPushButton tên btnLogin)
        self.pushButton_Login.clicked.connect(self.handle_login)

    def showWindow(self):
        self.MainWindow.show()

    def handle_login(self):
        # Lấy username và password từ QLineEdit (giả sử tên các trường là lineEditUsername và lineEditPassword)
        username = self.lineEditEmail.text().strip()
        password = self.lineEdit_Password.text().strip()

        user = self.login_customer(username, password)
        if user:
            QMessageBox.information(self.MainWindow, "Thành công",
                                    f"Đăng nhập thành công! Chào mừng {user.get('name')}")
            # Tại đây bạn có thể chuyển qua cửa sổ quản lý, ví dụ:
            # self.MainWindow.close()
            # mở MainWindowManagement
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def login_customer(self, username, password):
        # So sánh thông tin đăng nhập với dữ liệu khách hàng đã tải
        for customer in self.customers:
            if customer.get("username") == username and customer.get("password") == password:
                return customer
        return None
