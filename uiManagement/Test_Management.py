from PyQt6.QtWidgets import QMainWindow, QApplication

from uiManagement.MainWindow_Management_EXT import Mainwindow_Management_EXT

app=QApplication([])
mainwindow=QMainWindow()
myui = Mainwindow_Management_EXT()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()