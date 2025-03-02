from uiManagement.MainWindow_Management import Ui_MainWindow


class Mainwindow_Management_EXT (Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonClear.clicked.connect(self.clear_in4)

    def clear_in4(self):
        self.lineEditRegion.clear()
        self.lineEditTable.clear()
        self.lineEditDate.clear()
        self.lineEditTime.clear()
        self.lineEdit_FName.clear()
        self.lineEdit_LName.clear()
        self.lineEdit_Email.clear()
        self.lineEdit_Mobile.clear()
        self.lineEdit_Note.clear()
        self.lineEdit_EmpName.clear()
        self.lineEditShift.clear()
        self.lineEditRegion.setFocus()
