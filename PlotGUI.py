# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 474)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 60, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = PlotWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(90, 130, 421, 271))
        self.widget.setObjectName("widget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Push to Plot"))

from matplotlibWidgetFile import PlotWidget
