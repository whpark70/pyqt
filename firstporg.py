import sys
from PyQt5.QtWidgets import QApplication, QDialog
from first import Ui_Dialog

class MyDialog(Ui_Dialog):
	def __init__(self, dialog):
		super().__init__()
		self.setupUi(dialog)

		self.addBtn.clicked.connect(self.addInputTextToListbox)

	def addInputTextToListbox(self):
		txt = self.myTextInput.text()
		self.listWidget.addItem(txt)
		self.myTextInput.clear()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	dialog = QDialog()

	mydialog = MyDialog(dialog)

	dialog.show()
	sys.exit(app.exec_())