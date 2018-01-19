# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listview.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(715, 459)
        self.stackWidget = QtWidgets.QStackedWidget(Form)
        self.stackWidget.setEnabled(True)
        self.stackWidget.setGeometry(QtCore.QRect(250, 80, 150, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackWidget.sizePolicy().hasHeightForWidth())
        self.stackWidget.setSizePolicy(sizePolicy)
        self.stackWidget.setBaseSize(QtCore.QSize(150, 200))
        self.stackWidget.setObjectName("stackWidget")
        self.widget_1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.widget_1.setObjectName("widget_1")
        self.pushButton = QtWidgets.QPushButton(self.widget_1)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.stackWidget.addWidget(self.widget_1)
        self.widget_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(50, 80, 54, 11))
        self.label.setObjectName("label")
        self.stackWidget.addWidget(self.widget_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(50, 70, 171, 221))
        self.groupBox.setObjectName("groupBox")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(10, 10, 150, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        self.stackWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "버튼1"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.groupBox.setTitle(_translate("Form", "List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

