from PyQt6.QtWidgets import QApplication, QMainWindow

from uiManagement.BookingManagementEx import BookingManagementEx

app=QApplication([])
main_window=QMainWindow()
ui=BookingManagementEx()
ui.setupUi(main_window)
main_window.show()
app.exec()