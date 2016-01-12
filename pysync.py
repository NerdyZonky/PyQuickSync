# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pysync.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_PySync(object):
    def setupUi(self, PySync):
        PySync.setObjectName(_fromUtf8("PySync"))
        PySync.resize(314, 203)
        self.lineEdit = QtGui.QLineEdit(PySync)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 221, 32))
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(PySync)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 60, 221, 32))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(PySync)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 20, 31, 31))
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(PySync)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 60, 31, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.progressBar = QtGui.QProgressBar(PySync)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(20, 150, 271, 26))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton = QtGui.QPushButton(PySync)
        self.pushButton.setGeometry(QtCore.QRect(90, 110, 119, 29))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(PySync)
        QtCore.QMetaObject.connectSlotsByName(PySync)

    def retranslateUi(self, PySync):
        PySync.setWindowTitle(_translate("PySync", "Dialog", None))
        self.lineEdit.setToolTip(_translate("PySync", "<html><head/><body><p>Geben Sie die Quelle an</p></body></html>", None))
        self.lineEdit.setPlaceholderText(_translate("PySync", "Quelle", None))
        self.lineEdit_2.setToolTip(_translate("PySync", "<html><head/><body><p>Geben Sie das Ziel an</p></body></html>", None))
        self.lineEdit_2.setPlaceholderText(_translate("PySync", "Ziel", None))
        self.pushButton_2.setText(_translate("PySync", "...", None))
        self.pushButton_3.setText(_translate("PySync", "...", None))
        self.pushButton.setText(_translate("PySync", "Sync", None))

