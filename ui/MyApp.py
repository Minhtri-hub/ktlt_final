from PyQt6.QtWidgets import QApplication, QMainWindow

from UILoginEx import MainWindowEx

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.showWindow()
app.exec()