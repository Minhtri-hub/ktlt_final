from PyQt6.QtWidgets import QApplication, QMainWindow

from UiBooking.BookingInformationEx import BookingInformationEx

app=QApplication([])
main_window=QMainWindow()
ui=BookingInformationEx()
ui.setupUi(main_window)
main_window.show()
app.exec()