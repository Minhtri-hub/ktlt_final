from uiManagement.MainWindow_Management import Ui_MainWindow


class Mainwindow_Management_EXT (Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def showWindow(self):
        self.MainWindow.show()