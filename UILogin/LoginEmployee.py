# Form implementation generated from reading ui file 'C:\Users\nguye\PycharmProjects\ktlt_final\UILogin\LoginEmployee.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1170, 994)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, -10, 521, 481))
        self.groupBox.setStyleSheet("background-color: rgb(239, 236, 212);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEditUsernameEmployee = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditUsernameEmployee.setGeometry(QtCore.QRect(60, 180, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(10)
        self.lineEditUsernameEmployee.setFont(font)
        self.lineEditUsernameEmployee.setStyleSheet("color: rgb(126, 126, 126);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditUsernameEmployee.setObjectName("lineEditUsernameEmployee")
        self.lineEditPasswordEmployee = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPasswordEmployee.setGeometry(QtCore.QRect(60, 270, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(10)
        self.lineEditPasswordEmployee.setFont(font)
        self.lineEditPasswordEmployee.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditPasswordEmployee.setObjectName("lineEditPasswordEmployee")
        self.pushButtonLoginEmployee = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonLoginEmployee.setGeometry(QtCore.QRect(180, 370, 181, 41))
        self.pushButtonLoginEmployee.setStyleSheet("background-color: rgb(117, 5, 68);\n"
"font: 63 13pt \"Sitka Small Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButtonLoginEmployee.setObjectName("pushButtonLoginEmployee")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\nguye\\PycharmProjects\\ktlt_final\\UILogin\\7791667_necktie_businessman_suit_manager_employee_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 20, 151, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Users\\nguye\\PycharmProjects\\ktlt_final\\UILogin\\309035_user_account_human_person_icon.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(24, 280, 21, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\nguye\\PycharmProjects\\ktlt_final\\UILogin\\9021590_password_bold_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1170, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEditUsernameEmployee.setText(_translate("MainWindow", " *USER NAME"))
        self.lineEditPasswordEmployee.setText(_translate("MainWindow", "*PASSWORD"))
        self.pushButtonLoginEmployee.setText(_translate("MainWindow", "Log in"))
