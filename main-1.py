import sys
from PyQt5.QtWidgets import QApplication, QWidget
from test import Ui_Form

class MyWidget(Ui_Form):
	def __init__(self,widget):
		super().__init__()
		self.setupUi(widget)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = QWidget()
	mywidget = MyWidget(widget)
	widget.show()
	sys.exit(app.exec_())
