from PyQt6.QtWidgets import QApplication, QMainWindow
from UILogin.LoginCustomerEx import LoginCustomerEx

app = QApplication([])
main_window = QMainWindow()
ui = LoginCustomerEx()
ui.setupUi(main_window)
main_window.show()
app.exec()
