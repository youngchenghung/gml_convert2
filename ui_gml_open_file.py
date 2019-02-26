# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gml_open_file.ui'
#
# Created: Tue Feb 26 11:06:57 2019
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_GmlOpenFile(object):
    def setupUi(self, GmlOpenFile):
        GmlOpenFile.setObjectName(_fromUtf8("GmlOpenFile"))
        GmlOpenFile.resize(329, 215)
        self.open_gml = QtGui.QPushButton(GmlOpenFile)
        self.open_gml.setGeometry(QtCore.QRect(220, 30, 81, 31))
        self.open_gml.setObjectName(_fromUtf8("open_gml"))
        self.cancel = QtGui.QPushButton(GmlOpenFile)
        self.cancel.setGeometry(QtCore.QRect(100, 160, 131, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.label_open_gml = QtGui.QLineEdit(GmlOpenFile)
        self.label_open_gml.setGeometry(QtCore.QRect(20, 30, 181, 31))
        self.label_open_gml.setObjectName(_fromUtf8("label_open_gml"))
        self.convert = QtGui.QPushButton(GmlOpenFile)
        self.convert.setGeometry(QtCore.QRect(100, 80, 131, 31))
        self.convert.setObjectName(_fromUtf8("convert"))
        self.convert_2 = QtGui.QPushButton(GmlOpenFile)
        self.convert_2.setGeometry(QtCore.QRect(100, 120, 131, 31))
        self.convert_2.setObjectName(_fromUtf8("convert_2"))

        self.retranslateUi(GmlOpenFile)
        QtCore.QMetaObject.connectSlotsByName(GmlOpenFile)

    def retranslateUi(self, GmlOpenFile):
        GmlOpenFile.setWindowTitle(_translate("GmlOpenFile", "GML檔案轉移", None))
        self.open_gml.setText(_translate("GmlOpenFile", "開啟", None))
        self.cancel.setText(_translate("GmlOpenFile", "取消", None))
        self.convert.setText(_translate("GmlOpenFile", "轉移", None))
        self.convert_2.setText(_translate("GmlOpenFile", "取得 FINSH_ID", None))

