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
        BookingInformation.resize(709, 732)
        self.centralwidget = QtWidgets.QWidget(parent=BookingInformation)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 10, 551, 581))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(240, 237, 213);")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 127, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
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
        self.lineEditFirstName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditFirstName.setGeometry(QtCore.QRect(140, 200, 371, 31))
        self.lineEditFirstName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditFirstName.setText("")
        self.lineEditFirstName.setPlaceholderText("")
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.lineEditLastName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditLastName.setGeometry(QtCore.QRect(140, 250, 371, 31))
        self.lineEditLastName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditLastName.setObjectName("lineEditLastName")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEmail.setGeometry(QtCore.QRect(140, 300, 371, 31))
        self.lineEditEmail.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditMobile = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditMobile.setGeometry(QtCore.QRect(140, 350, 371, 31))
        self.lineEditMobile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditMobile.setObjectName("lineEditMobile")
        self.lineEditSpecialNote = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditSpecialNote.setGeometry(QtCore.QRect(140, 400, 371, 101))
        self.lineEditSpecialNote.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.lineEditSpecialNote.setObjectName("lineEditSpecialNote")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 450, 47, 14))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.checkBoxReceiveMenu = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBoxReceiveMenu.setGeometry(QtCore.QRect(50, 520, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(9)
        self.checkBoxReceiveMenu.setFont(font)
        self.checkBoxReceiveMenu.setObjectName("checkBoxReceiveMenu")
        self.checkBoxConfirmBooking = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBoxConfirmBooking.setGeometry(QtCore.QRect(50, 550, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(9)
        self.checkBoxConfirmBooking.setFont(font)
        self.checkBoxConfirmBooking.setObjectName("checkBoxConfirmBooking")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 561, 81))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(0, 54, 0);\n"
"")
        self.label_8.setObjectName("label_8")
        self.frame = QtWidgets.QFrame(parent=self.groupBox)
        self.frame.setGeometry(QtCore.QRect(20, 100, 511, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/.designer/backup/images/ic_table.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.labelSeatingArea = QtWidgets.QLabel(parent=self.frame)
        self.labelSeatingArea.setGeometry(QtCore.QRect(50, 10, 341, 31))
        self.labelSeatingArea.setText("")
        self.labelSeatingArea.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/Downloads/8508747_eating_placesrestaurant_table_restaurant_food_icon.png"))
        self.labelSeatingArea.setObjectName("labelSeatingArea")
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 41, 31))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/.designer/backup/images/ic_people.png"))
        self.label_10.setObjectName("label_10")
        self.label1 = QtWidgets.QLabel(parent=self.frame)
        self.label1.setGeometry(QtCore.QRect(200, 40, 41, 41))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/.designer/backup/images/ic_calendar.png"))
        self.label1.setScaledContents(False)
        self.label1.setObjectName("label1")
        self.labelNumberOfPeople = QtWidgets.QLabel(parent=self.frame)
        self.labelNumberOfPeople.setGeometry(QtCore.QRect(50, 50, 141, 31))
        self.labelNumberOfPeople.setText("")
        self.labelNumberOfPeople.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/Downloads/309041_users_group_people_icon.png"))
        self.labelNumberOfPeople.setObjectName("labelNumberOfPeople")
        self.labelDateTime = QtWidgets.QLabel(parent=self.frame)
        self.labelDateTime.setGeometry(QtCore.QRect(240, 50, 141, 31))
        self.labelDateTime.setText("")
        self.labelDateTime.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/Downloads/8664801_calendar_icon.png"))
        self.labelDateTime.setObjectName("labelDateTime")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(240, 30, 21, 21))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 54, 0);")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/Downloads/lotus_2982182 (1).png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(90, 590, 551, 91))
        self.groupBox_2.setStyleSheet("background-color: rgb(240, 237, 213);\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(120, 10, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
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
        BookingInformation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=BookingInformation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 18))
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
        self.groupBox.setTitle(_translate("BookingInformation", "GroupBox"))
        self.label_3.setText(_translate("BookingInformation", "First Name: "))
        self.label_2.setText(_translate("BookingInformation", "Last Name:"))
        self.label.setText(_translate("BookingInformation", "Email:"))
        self.label_4.setText(_translate("BookingInformation", "Mobile:"))
        self.label_5.setText(_translate("BookingInformation", "Special Note:"))
        self.lineEditEmail.setPlaceholderText(_translate("BookingInformation", "...@gmail.com"))
        self.lineEditMobile.setPlaceholderText(_translate("BookingInformation", "+84"))
        self.lineEditSpecialNote.setPlaceholderText(_translate("BookingInformation", "e.g. Anniversary, birthday, allergies,..."))
        self.checkBoxReceiveMenu.setText(_translate("BookingInformation", "Yes! I want to receive newsletter about Lotus menus, promotions and events."))
        self.checkBoxConfirmBooking.setText(_translate("BookingInformation", "Confirm Booking (Send Email or SMS Notification)"))
        self.label_8.setText(_translate("BookingInformation", "<html><head/><body><p align=\"center\"><span style=\" color:#faf2ea;\">LOTUS</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("BookingInformation", "GroupBox"))
        self.label_7.setText(_translate("BookingInformation", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">By clicking this button, I agreed with these General Term &amp; Conditions</span></p></body></html>"))
        self.pushButtonBookingTable.setText(_translate("BookingInformation", "Booking Your Table"))
