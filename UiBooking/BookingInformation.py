# Form implementation generated from reading ui file 'C:\Users\nguye\PycharmProjects\ktlt_final\UiBooking\BookingInformation.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BookingInformation(object):
    def setupUi(self, BookingInformation):
        BookingInformation.setObjectName("BookingInformation")
        BookingInformation.resize(1572, 1221)
        self.centralwidget = QtWidgets.QWidget(parent=BookingInformation)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(350, 100, 551, 581))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(240, 237, 213);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 127, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEditFullName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditFullName.setGeometry(QtCore.QRect(150, 170, 371, 31))
        self.lineEditFullName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditFullName.setText("")
        self.lineEditFullName.setPlaceholderText("")
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEmail.setGeometry(QtCore.QRect(150, 240, 371, 31))
        self.lineEditEmail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditMobile = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditMobile.setGeometry(QtCore.QRect(150, 300, 371, 31))
        self.lineEditMobile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditMobile.setObjectName("lineEditMobile")
        self.lineEditSpecialNote = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditSpecialNote.setGeometry(QtCore.QRect(150, 350, 371, 111))
        self.lineEditSpecialNote.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditSpecialNote.setObjectName("lineEditSpecialNote")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 450, 47, 14))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.checkBoxReceiveMenu = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBoxReceiveMenu.setGeometry(QtCore.QRect(60, 490, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(9)
        self.checkBoxReceiveMenu.setFont(font)
        self.checkBoxReceiveMenu.setObjectName("checkBoxReceiveMenu")
        self.checkBoxConfirmBooking = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBoxConfirmBooking.setGeometry(QtCore.QRect(100, 530, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(9)
        self.checkBoxConfirmBooking.setFont(font)
        self.checkBoxConfirmBooking.setObjectName("checkBoxConfirmBooking")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 561, 111))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(0, 54, 0);\n"
"")
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 680, 551, 91))
        self.groupBox_2.setStyleSheet("background-color: rgb(240, 237, 213);\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonBookingTable = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonBookingTable.setGeometry(QtCore.QRect(150, 40, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBookingTable.setFont(font)
        self.pushButtonBookingTable.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonBookingTable.setObjectName("pushButtonBookingTable")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(120, 10, 341, 16))
        self.label_7.setObjectName("label_7")
        BookingInformation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=BookingInformation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1572, 26))
        self.menubar.setObjectName("menubar")
        BookingInformation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=BookingInformation)
        self.statusbar.setObjectName("statusbar")
        BookingInformation.setStatusBar(self.statusbar)

        self.retranslateUi(BookingInformation)
        QtCore.QMetaObject.connectSlotsByName(BookingInformation)

    def retranslateUi(self, BookingInformation):
        _translate = QtCore.QCoreApplication.translate
        BookingInformation.setWindowTitle(_translate("BookingInformation", "Booking Information"))
        self.label_2.setText(_translate("BookingInformation", "Full Name:"))
        self.label.setText(_translate("BookingInformation", "Email:"))
        self.label_4.setText(_translate("BookingInformation", "Mobile:"))
        self.label_5.setText(_translate("BookingInformation", "Special Note:"))
        self.lineEditEmail.setPlaceholderText(_translate("BookingInformation", "...@gmail.com"))
        self.lineEditMobile.setPlaceholderText(_translate("BookingInformation", "+84"))
        self.lineEditSpecialNote.setPlaceholderText(_translate("BookingInformation", "e.g. Anniversary, birthday, allergies,..."))
        self.checkBoxReceiveMenu.setText(_translate("BookingInformation", "Yes! I want to receive newsletter about Lotus menus, promotions and events."))
        self.checkBoxConfirmBooking.setText(_translate("BookingInformation", "Confirm Booking (Send Email or SMS Notification)"))
        self.label_8.setText(_translate("BookingInformation", "<html><head/><body><p align=\"center\"><span style=\" color:#faf2ea;\">LOTUS</span></p></body></html>"))
        self.pushButtonBookingTable.setText(_translate("BookingInformation", "Booking Your Table"))
        self.label_7.setText(_translate("BookingInformation", "By clicking this button, I agreed with these General Term & Conditions"))
