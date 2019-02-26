# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_drop_zd.ui'
#
# Created: Tue Feb 19 16:32:20 2019
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

class Ui_DropZD(object):
    def setupUi(self, DropZD):
        DropZD.setObjectName(_fromUtf8("DropZD"))
        DropZD.resize(385, 174)
        self.label_open_gml_to_shp = QtGui.QLineEdit(DropZD)
        self.label_open_gml_to_shp.setGeometry(QtCore.QRect(40, 30, 211, 41))
        self.label_open_gml_to_shp.setObjectName(_fromUtf8("label_open_gml_to_shp"))
        self.open_gml_to_shp = QtGui.QPushButton(DropZD)
        self.open_gml_to_shp.setGeometry(QtCore.QRect(270, 30, 81, 41))
        self.open_gml_to_shp.setObjectName(_fromUtf8("open_gml_to_shp"))
        self.drop_zd = QtGui.QPushButton(DropZD)
        self.drop_zd.setGeometry(QtCore.QRect(70, 110, 121, 31))
        self.drop_zd.setObjectName(_fromUtf8("drop_zd"))
        self.cancel = QtGui.QPushButton(DropZD)
        self.cancel.setGeometry(QtCore.QRect(210, 110, 121, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(DropZD)
        QtCore.QMetaObject.connectSlotsByName(DropZD)

    def retranslateUi(self, DropZD):
        DropZD.setWindowTitle(_translate("DropZD", "三維轉二維", None))
        self.open_gml_to_shp.setText(_translate("DropZD", "瀏覽", None))
        self.drop_zd.setText(_translate("DropZD", "轉移", None))
        self.cancel.setText(_translate("DropZD", "取消", None))

