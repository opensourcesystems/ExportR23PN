# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExportR23PN.ui'
#
# Created: Thu Mar 28 18:12:43 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(745, 376)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(0, 120, 731, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(0, 90, 641, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(650, 90, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 150, 731, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 350, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 271, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.samsonadr = QtGui.QLineEdit(self.groupBox)
        self.samsonadr.setGeometry(QtCore.QRect(50, 20, 71, 20))
        self.samsonadr.setObjectName(_fromUtf8("samsonadr"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 41, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.samsonbd = QtGui.QLineEdit(self.groupBox)
        self.samsonbd.setGeometry(QtCore.QRect(50, 50, 71, 20))
        self.samsonbd.setObjectName(_fromUtf8("samsonbd"))
        self.samsonlogin = QtGui.QLineEdit(self.groupBox)
        self.samsonlogin.setGeometry(QtCore.QRect(170, 20, 81, 20))
        self.samsonlogin.setObjectName(_fromUtf8("samsonlogin"))
        self.samsonpassword = QtGui.QLineEdit(self.groupBox)
        self.samsonpassword.setGeometry(QtCore.QRect(170, 50, 81, 20))
        self.samsonpassword.setObjectName(_fromUtf8("samsonpassword"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 0, 461, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 20, 51, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.smo_cmbx = QtGui.QComboBox(self.groupBox_2)
        self.smo_cmbx.setGeometry(QtCore.QRect(10, 50, 441, 22))
        self.smo_cmbx.setObjectName(_fromUtf8("smo_cmbx"))
        self.smo_codes = QtGui.QLineEdit(self.groupBox_2)
        self.smo_codes.setGeometry(QtCore.QRect(140, 20, 311, 20))
        self.smo_codes.setObjectName(_fromUtf8("smo_codes"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "ExportR23PN", None))
        self.pushButton.setText(_translate("Dialog", "Путь", None))
        self.pushButton_2.setText(_translate("Dialog", "Экспорт", None))
        self.groupBox.setTitle(_translate("Dialog", "Samson", None))
        self.samsonadr.setText(_translate("Dialog", "127.0.0.1", None))
        self.label.setText(_translate("Dialog", "Адрес", None))
        self.label_2.setText(_translate("Dialog", "База", None))
        self.label_3.setText(_translate("Dialog", "Логин", None))
        self.label_4.setText(_translate("Dialog", "Пароль", None))
        self.samsonbd.setText(_translate("Dialog", "s11", None))
        self.samsonlogin.setText(_translate("Dialog", "root", None))
        self.samsonpassword.setText(_translate("Dialog", "Qwedsa1!", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Выгрузить в", None))
        self.radioButton.setText(_translate("Dialog", "МИАЦ", None))
        self.radioButton_2.setText(_translate("Dialog", "СМО", None))
        self.smo_codes.setText(_translate("Dialog", "или Введите коды СМО через запятую", None))

