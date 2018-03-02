import sys
from PyQt5.QtCore import QUrl, Qt, QModelIndex, QAbstractItemModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication, QListView, QStyledItemDelegate
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext

class SampleModel(QStandardItemModel):
	#NodeRole = Qt.UserRole + 1
	def __init__(self):
		super().__init__()
		#self.nodes = [ 'srv1', 'srv2', 'srv3']
		
		self.nodes = {
					"Servers": ['srv1', 'srv2', 'srv3'],
					"Network": [ 'UTM-1', "UTM-2", "Switch-01"]
			}
		
		if self.nodes != None:
			for node, subnode in self.nodes.items():
				node_item = QStandardItem()
				node_item.setData(node, Qt.UserRole+1)
				self.appendRow(node_item)
		
				if type(subnode) == list:
					for row, snode in enumerate(subnode):
						snode_item = QStandardItem()
						snode_item.setData(subnode, Qt.UserRole+1)
						node_item.appendRow(snode_item)
		

class SampleDelgate(QStyledItemDelegate):
	"""docstring for sampleItemDelgate"""
	def __init__(self):
		super().__init__()
		
	def paint(self, painter, option, index):
		print(index.data(Qt.UserRole + 1).hasChildren())
		self.initStyleOption(option, index)
		print(option.text)
		return QStyledItemDelegate.paint(self, painter, option, index)


def main():

	app = QApplication(sys.argv)

	model = SampleModel()
	delegate = SampleDelgate()
	view = QListView()
	view.setModel(model)
	view.setItemDelegate(delegate)

	view.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
