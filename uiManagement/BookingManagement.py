# Form implementation generated from reading ui file 'C:\Users\nguye\PycharmProjects\ktlt_final\uiManagement\BookingManagement.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 820)
        MainWindow.setStyleSheet("background-color: rgb(240, 237, 213);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1441, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 54, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(680, 60, 751, 721))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidgetBookingList = QtWidgets.QTableWidget(parent=self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.tableWidgetBookingList.setFont(font)
        self.tableWidgetBookingList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetBookingList.setObjectName("tableWidgetBookingList")
        self.tableWidgetBookingList.setColumnCount(9)
        self.tableWidgetBookingList.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetBookingList.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetBookingList.setItem(5, 5, item)
        self.horizontalLayout.addWidget(self.tableWidgetBookingList)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 60, 661, 451))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditBookingID = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditBookingID.setGeometry(QtCore.QRect(110, 30, 211, 31))
        self.lineEditBookingID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditBookingID.setObjectName("lineEditBookingID")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditPeople = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditPeople.setGeometry(QtCore.QRect(90, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditPeople.setFont(font)
        self.lineEditPeople.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditPeople.setObjectName("lineEditPeople")
        self.lineEditCustomerID = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditCustomerID.setGeometry(QtCore.QRect(440, 30, 211, 31))
        self.lineEditCustomerID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditCustomerID.setObjectName("lineEditCustomerID")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(340, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditDate = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditDate.setGeometry(QtCore.QRect(270, 180, 131, 31))
        self.lineEditDate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditDate.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditDate.setObjectName("lineEditDate")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(210, 180, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEditTime = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditTime.setGeometry(QtCore.QRect(490, 180, 141, 31))
        self.lineEditTime.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditTime.setObjectName("lineEditTime")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(430, 180, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(10, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.comboBoxSeatingType = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.comboBoxSeatingType.setGeometry(QtCore.QRect(110, 240, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(11)
        self.comboBoxSeatingType.setFont(font)
        self.comboBoxSeatingType.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.comboBoxSeatingType.setObjectName("comboBoxSeatingType")
        self.comboBoxSeatingType.addItem("")
        self.comboBoxSeatingType.addItem("")
        self.lineEditFirstName = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditFirstName.setGeometry(QtCore.QRect(110, 80, 211, 31))
        self.lineEditFirstName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditLastName = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditLastName.setGeometry(QtCore.QRect(440, 80, 211, 31))
        self.lineEditLastName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditLastName.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditLastName.setObjectName("lineEditLastName")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(340, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEditMobile = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditMobile.setGeometry(QtCore.QRect(440, 130, 211, 31))
        self.lineEditMobile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditMobile.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditMobile.setObjectName("lineEditMobile")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(340, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditEmail.setGeometry(QtCore.QRect(110, 130, 211, 31))
        self.lineEditEmail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditSpecial = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEditSpecial.setGeometry(QtCore.QRect(110, 340, 531, 91))
        self.lineEditSpecial.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditSpecial.setObjectName("lineEditSpecial")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBoxStatus = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.comboBoxStatus.setGeometry(QtCore.QRect(110, 290, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(11)
        self.comboBoxStatus.setFont(font)
        self.comboBoxStatus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.comboBoxStatus.setObjectName("comboBoxStatus")
        self.comboBoxStatus.addItem("")
        self.comboBoxStatus.addItem("")
        self.comboBoxStatus.addItem("")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(10, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 710, 671, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButtonClear.setGeometry(QtCore.QRect(20, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setStyleSheet("background-color: rgb(117, 5, 68);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonSaveNew = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButtonSaveNew.setGeometry(QtCore.QRect(190, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSaveNew.setFont(font)
        self.pushButtonSaveNew.setStyleSheet("background-color: rgb(117, 5, 68);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonSaveNew.setObjectName("pushButtonSaveNew")
        self.pushButtonsaveUpdate = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButtonsaveUpdate.setGeometry(QtCore.QRect(370, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonsaveUpdate.setFont(font)
        self.pushButtonsaveUpdate.setStyleSheet("background-color: rgb(117, 5, 68);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonsaveUpdate.setObjectName("pushButtonsaveUpdate")
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButtonDelete.setGeometry(QtCore.QRect(550, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setStyleSheet("background-color: rgb(117, 5, 68);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 520, 661, 181))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPassword.setGeometry(QtCore.QRect(440, 80, 211, 31))
        self.lineEditPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(330, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEditUserName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditUserName.setGeometry(QtCore.QRect(110, 80, 211, 31))
        self.lineEditUserName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditEmployeeID = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEmployeeID.setGeometry(QtCore.QRect(110, 30, 211, 31))
        self.lineEditEmployeeID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditEmployeeID.setObjectName("lineEditEmployeeID")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(330, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEditEmployeeName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEmployeeName.setGeometry(QtCore.QRect(440, 30, 211, 31))
        self.lineEditEmployeeName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditEmployeeName.setObjectName("lineEditEmployeeName")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(10, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.comboBoxRole = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBoxRole.setGeometry(QtCore.QRect(110, 130, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(11)
        self.comboBoxRole.setFont(font)
        self.comboBoxRole.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 0, 0);")
        self.comboBoxRole.setObjectName("comboBoxRole")
        self.comboBoxRole.addItem("")
        self.comboBoxRole.addItem("")
        self.lineEditShift = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditShift.setGeometry(QtCore.QRect(440, 130, 211, 31))
        self.lineEditShift.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditShift.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditShift.setObjectName("lineEditShift")
        self.label_24 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(330, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala Text Semilight")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_19 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1380, 440, 61, 61))
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(239, 236, 212);")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/Downloads/lotus_2982182 (1).png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LeThiMyHoa - K234111389"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">BOOKING MANAGAMENT</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Booking Lists:"))
        item = self.tableWidgetBookingList.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidgetBookingList.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidgetBookingList.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidgetBookingList.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidgetBookingList.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidgetBookingList.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Booking ID"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Customer ID"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Customer Name"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "People"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Table ID"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Seating Type"))
        item = self.tableWidgetBookingList.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Status"))
        __sortingEnabled = self.tableWidgetBookingList.isSortingEnabled()
        self.tableWidgetBookingList.setSortingEnabled(False)
        self.tableWidgetBookingList.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("MainWindow", "Booking Detail:"))
        self.label_2.setText(_translate("MainWindow", "Booking ID:"))
        self.label_3.setText(_translate("MainWindow", "People:"))
        self.label_4.setText(_translate("MainWindow", "Customer ID:"))
        self.label_8.setText(_translate("MainWindow", "Date:"))
        self.label_15.setText(_translate("MainWindow", "Time:"))
        self.label_16.setText(_translate("MainWindow", "Seating Type:"))
        self.comboBoxSeatingType.setCurrentText(_translate("MainWindow", "Counter Seating"))
        self.comboBoxSeatingType.setItemText(0, _translate("MainWindow", "Counter Seating"))
        self.comboBoxSeatingType.setItemText(1, _translate("MainWindow", "Private Dining Room"))
        self.label_5.setText(_translate("MainWindow", "First Name:"))
        self.label_10.setText(_translate("MainWindow", "Last Name:"))
        self.label_6.setText(_translate("MainWindow", "Email:"))
        self.label_11.setText(_translate("MainWindow", "Mobile:"))
        self.label_7.setText(_translate("MainWindow", "Special Note:"))
        self.comboBoxStatus.setCurrentText(_translate("MainWindow", "Confirmed "))
        self.comboBoxStatus.setItemText(0, _translate("MainWindow", "Confirmed "))
        self.comboBoxStatus.setItemText(1, _translate("MainWindow", "Pending"))
        self.comboBoxStatus.setItemText(2, _translate("MainWindow", "Cancelled"))
        self.label_17.setText(_translate("MainWindow", "Status:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Employee Action:"))
        self.pushButtonClear.setText(_translate("MainWindow", "Clear"))
        self.pushButtonSaveNew.setText(_translate("MainWindow", "Save New"))
        self.pushButtonsaveUpdate.setText(_translate("MainWindow", "Save Update"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete"))
        self.groupBox.setTitle(_translate("MainWindow", "Employee Detail:"))
        self.label_9.setText(_translate("MainWindow", "Employee\'s Name:"))
        self.label_12.setText(_translate("MainWindow", "Employee ID:"))
        self.label_13.setText(_translate("MainWindow", "UserName:"))
        self.label_14.setText(_translate("MainWindow", "Password:"))
        self.label_18.setText(_translate("MainWindow", "Role:"))
        self.comboBoxRole.setCurrentText(_translate("MainWindow", "Manager"))
        self.comboBoxRole.setItemText(0, _translate("MainWindow", "Manager"))
        self.comboBoxRole.setItemText(1, _translate("MainWindow", "Staff"))
        self.label_24.setText(_translate("MainWindow", "Shift:"))
