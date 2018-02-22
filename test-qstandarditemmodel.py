import sys
from PyQt5.QtCore import QUrl, Qt, QModelIndex, QAbstractItemModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext

class SampleModel(QStandardItemModel):
	#NodeRole = Qt.UserRole + 1
	def __init__(self):
		super().__init__()
		self.nodes = {
					"Servers": ['srv1', 'srv2', 'srv3'],
					"Network": [ 'UTM-1', "UTM-2", "Switch-01"]
			}

		if self.nodes != None:
			for node, subnode in self.nodes.items():
				node_item = QStandardItem(node)
				self.appendRow(node_item)

				if type(subnode) == list:
					for row, snode in enumerate(subnode):
						snode_item = QStandardItem(snode)
						node_item.setChild(row, snode_item)

def main():

	model = SampleModel()
	_rp = model.invisibleRootItem()
	
	if _rp.hasChildren():
		print('row count: ', _rp.rowCount())
		for i in range(_rp.rowCount()):
			print()
			print(_rp.child(i).text() + ': ' , end = ' ')
			if _rp.child(i).hasChildren():
				for j in range(_rp.child(i).rowCount()):
					print(_rp.child(i).child(j).text(), end=' ')
	print()

	'''	
	print(model.item(0).text())
	print(model.item(0).hasChildren())
	print(model.item(0).child(0).text())
	'''

if __name__ == '__main__':
	main()