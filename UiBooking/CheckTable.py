# Form implementation generated from reading ui file 'D:\Sophomores (2nd semester)\Programming Techniques\GITHUB FINAL\UiBooking\CheckTable.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 848)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(110, 10, 521, 581))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 130, 71, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.dateEditDate = QtWidgets.QDateEdit(parent=self.groupBox)
        self.dateEditDate.setGeometry(QtCore.QRect(130, 190, 331, 31))
        self.dateEditDate.setMaximumDate(QtCore.QDate(2025, 12, 31))
        self.dateEditDate.setMinimumDate(QtCore.QDate(2025, 1, 1))
        self.dateEditDate.setCalendarPopup(True)
        self.dateEditDate.setObjectName("dateEditDate")
        self.comboBoxPeople = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBoxPeople.setGeometry(QtCore.QRect(130, 140, 331, 31))
        self.comboBoxPeople.setEditable(True)
        self.comboBoxPeople.setMaxCount(20)
        self.comboBoxPeople.setObjectName("comboBoxPeople")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.comboBoxPeople.addItem("")
        self.radioButtonCounterSeating = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButtonCounterSeating.setGeometry(QtCore.QRect(130, 290, 151, 41))
        self.radioButtonCounterSeating.setObjectName("radioButtonCounterSeating")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 380, 221, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(150, 430, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(150, 320, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButtonCheckAvailability = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonCheckAvailability.setGeometry(QtCore.QRect(110, 490, 321, 41))
        self.pushButtonCheckAvailability.setObjectName("pushButtonCheckAvailability")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(150, 340, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(150, 410, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBoxTime = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBoxTime.setGeometry(QtCore.QRect(130, 240, 331, 31))
        self.comboBoxTime.setEditable(True)
        self.comboBoxTime.setMaxCount(20)
        self.comboBoxTime.setObjectName("comboBoxTime")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 40, 411, 61))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 22))
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
        self.groupBox.setTitle(_translate("MainWindow", "Book Your Table:"))
        self.label_3.setText(_translate("MainWindow", "People:"))
        self.label_2.setText(_translate("MainWindow", "Date:"))
        self.label_4.setText(_translate("MainWindow", "Time:"))
        self.dateEditDate.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.comboBoxPeople.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxPeople.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxPeople.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxPeople.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxPeople.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxPeople.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxPeople.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxPeople.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxPeople.setItemText(8, _translate("MainWindow", "9"))
        self.comboBoxPeople.setItemText(9, _translate("MainWindow", "10"))
        self.comboBoxPeople.setItemText(10, _translate("MainWindow", "11"))
        self.comboBoxPeople.setItemText(11, _translate("MainWindow", "12"))
        self.comboBoxPeople.setItemText(12, _translate("MainWindow", "13"))
        self.comboBoxPeople.setItemText(13, _translate("MainWindow", "14"))
        self.comboBoxPeople.setItemText(14, _translate("MainWindow", "15"))
        self.comboBoxPeople.setItemText(15, _translate("MainWindow", "16"))
        self.comboBoxPeople.setItemText(16, _translate("MainWindow", "17"))
        self.comboBoxPeople.setItemText(17, _translate("MainWindow", "18"))
        self.comboBoxPeople.setItemText(18, _translate("MainWindow", "19"))
        self.comboBoxPeople.setItemText(19, _translate("MainWindow", "20"))
        self.radioButtonCounterSeating.setText(_translate("MainWindow", "Counter Seating"))
        self.radioButton_2.setText(_translate("MainWindow", "Private Dining Room"))
        self.label_5.setText(_translate("MainWindow", "can be arranged for up to 20 guests."))
        self.label_6.setText(_translate("MainWindow", "Counter Seating (1st Floor) – Chef’s Table Experience, "))
        self.pushButtonCheckAvailability.setText(_translate("MainWindow", "Check Availability"))
        self.label_7.setText(_translate("MainWindow", "can be arranged for up to 10 guests."))
        self.label_8.setText(_translate("MainWindow", "Private dining rooms (2nd Floor) – Exclusive & Intimate,"))
        self.comboBoxTime.setItemText(0, _translate("MainWindow", "4:00 PM"))
        self.comboBoxTime.setItemText(1, _translate("MainWindow", "4:15 PM"))
        self.comboBoxTime.setItemText(2, _translate("MainWindow", "4:30 PM"))
        self.comboBoxTime.setItemText(3, _translate("MainWindow", "4:45 PM"))
        self.comboBoxTime.setItemText(4, _translate("MainWindow", "5:00 PM"))
        self.comboBoxTime.setItemText(5, _translate("MainWindow", "5:15 PM"))
        self.comboBoxTime.setItemText(6, _translate("MainWindow", "5:30 PM"))
        self.comboBoxTime.setItemText(7, _translate("MainWindow", "5:45 PM"))
        self.comboBoxTime.setItemText(8, _translate("MainWindow", "6:00 PM"))
        self.comboBoxTime.setItemText(9, _translate("MainWindow", "6:15 PM"))
        self.comboBoxTime.setItemText(10, _translate("MainWindow", "6:30 PM"))
        self.comboBoxTime.setItemText(11, _translate("MainWindow", "6:45 PM"))
        self.comboBoxTime.setItemText(12, _translate("MainWindow", "7:00 PM"))
        self.comboBoxTime.setItemText(13, _translate("MainWindow", "7:15 PM"))
        self.comboBoxTime.setItemText(14, _translate("MainWindow", "7:30 PM"))
        self.comboBoxTime.setItemText(15, _translate("MainWindow", "7:45 PM"))
        self.comboBoxTime.setItemText(16, _translate("MainWindow", "8:00 PM"))
        self.comboBoxTime.setItemText(17, _translate("MainWindow", "8:15 PM"))
        self.comboBoxTime.setItemText(18, _translate("MainWindow", "8:30 PM"))
        self.comboBoxTime.setItemText(19, _translate("MainWindow", "10:30 PM"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55aaff;\">RESERVATION</span></p></body></html>"))
