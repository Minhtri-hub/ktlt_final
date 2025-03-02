from PyQt6.QtWidgets import QApplication, QMainWindow
from UILogin.LoginCustomerEx import LoginCustomerEx  # Giả sử đây là lớp giao diện do pyuic6 tạo ra

app = QApplication([])

# Tạo instance của QMainWindow
main_window = QMainWindow()

# Tạo instance của lớp giao diện và setup UI cho main_window
ui = LoginCustomerEx()
ui.setupUi(main_window)

# Hiển thị cửa sổ chính
main_window.show()

app.exec()
