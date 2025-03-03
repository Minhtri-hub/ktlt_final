from PyQt6.QtWidgets import QApplication, QMainWindow
from UiBooking.CheckTableEx import CheckTableEx  # Giả sử đây là lớp giao diện do pyuic6 tạo ra

app = QApplication([])
main_window = QMainWindow()
ui = CheckTableEx()
ui.setupUi(main_window)
main_window.show()
app.exec()
