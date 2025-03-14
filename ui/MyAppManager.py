from PyQt6.QtWidgets import QApplication, QMainWindow

from uiManagement.ManagementEx import ManagementEx

app=QApplication([])
main_window=QMainWindow()
ui=ManagementEx()
ui.setupUi(main_window)
main_window.show()
app.exec()