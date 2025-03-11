from PyQt6.QtWidgets import QApplication, QMainWindow
from UILogin.SignupEx import SignupEx  # Giả sử đây là lớp giao diện do pyuic6 tạo ra

app = QApplication([])
main_window = QMainWindow()
ui = SignupEx()
ui.setupUi(main_window)
main_window.show()
app.exec()
