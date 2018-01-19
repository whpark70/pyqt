# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(441, 301)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 381, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.myTextInput = QtWidgets.QLineEdit(Dialog)
        self.myTextInput.setGeometry(QtCore.QRect(20, 20, 131, 21))
        self.myTextInput.setObjectName("myTextInput")
        self.addBtn = QtWidgets.QPushButton(Dialog)
        self.addBtn.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.addBtn.setObjectName("addBtn")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(160, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.clearBtn = QtWidgets.QPushButton(Dialog)
        self.clearBtn.setGeometry(QtCore.QRect(20, 190, 75, 23))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.clearBtn.clicked.connect(self.listWidget.clear)
        self.clearBtn.clicked.connect(self.myTextInput.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addBtn.setText(_translate("Dialog", "add"))
        self.clearBtn.setText(_translate("Dialog", "clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

