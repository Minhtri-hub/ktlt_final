# Form implementation generated from reading ui file 'D:\ktlt_final\UILogin\Login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 855)
        MainWindow.setAccessibleName("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 10, 661, 761))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, -30, 461, 141))
        self.label.setObjectName("label")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEmail.setGeometry(QtCore.QRect(130, 170, 421, 31))
        self.lineEditEmail.setStatusTip("")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEdit_Password = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Password.setGeometry(QtCore.QRect(130, 250, 421, 31))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(320, 420, 101, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(260, 500, 55, 16))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(80, 580, 531, 121))
        self.checkBox.setObjectName("checkBox")
        self.pushButtonPhone = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonPhone.setGeometry(QtCore.QRect(130, 470, 421, 51))
        self.pushButtonPhone.setObjectName("pushButtonPhone")
        self.pushButton_Google = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_Google.setGeometry(QtCore.QRect(130, 550, 421, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/HUYNHNHI/Downloads/2993685_brand_brands_google_logo_logos_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Google.setIcon(icon)
        self.pushButton_Google.setObjectName("pushButton_Google")
        self.pushButton_Login = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_Login.setGeometry(QtCore.QRect(210, 340, 261, 51))
        self.pushButton_Login.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Login.setObjectName("pushButton_Login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 26))
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
        self.groupBox.setAccessibleDescription(_translate("MainWindow", "<html><head/><body><p>* Địa chỉ Email</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#00007f;\">Đăng Nhập</span></p></body></html>"))
        self.lineEditEmail.setAccessibleDescription(_translate("MainWindow", "* Địa chỉ Email"))
        self.lineEdit_Password.setAccessibleDescription(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#888888;\">* Mật Khẩu</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#00007f;\">Hoặc</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Tôi đã đọc và đồng ý các Chính sách bảo mật, Điều khoản & Điều kiện của PIZZA 5P\'S"))
        self.pushButtonPhone.setText(_translate("MainWindow", "Đăng nhập bằng số điện thoại"))
        self.pushButton_Google.setText(_translate("MainWindow", "Đăng nhập bằng Google"))
        self.pushButton_Login.setText(_translate("MainWindow", "Đăng nhập"))
