import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import pyqtSlot, QModelIndex
from listview import Ui_Form

class MyListView(Ui_Form):
	def __init__(self, widget):
		super().__init__()
		self.setupUi(widget)
		self.init_widget()

	def init_widget(self):
	
		list_title = [ '서버', '네트워크']
		
		model = QStandardItemModel()
		for item in list_title:
			model.appendRow(QStandardItem(item))

		self.listView.setModel(model)

		self.listView.clicked.connect(self.selectWidget)

	pyqtSlot(QModelIndex)
	def selectWidget(self, index):
		self.stackWidget.setCurrentIndex(index.row())
		

if __name__ == "__main__":

    app = QApplication(sys.argv)
    Form = QWidget()
    mylistview = MyListView(Form)

    Form.show()
    sys.exit(app.exec_())