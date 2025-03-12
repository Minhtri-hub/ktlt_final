from PyQt6.QtWidgets import QApplication, QMainWindow
from UILogin.LoginEmployeeEx import LoginEmployeeEx

app = QApplication([])
main_window = QMainWindow()
ui = LoginEmployeeEx()
ui.setupUi(main_window)
main_window.show()
app.exec()
