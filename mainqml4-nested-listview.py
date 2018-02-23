import sys
from PyQt5.QtCore import QUrl, Qt, QModelIndex, QAbstractItemModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext

class SampleModel(QStandardItemModel):
	NodeRole = Qt.UserRole + 1
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
	
	def data(self, index=None, role=Qt.DisplayRole):
		return self.item(index.row()).text()
	
	def roleNames(self):
		return { SampleModel.NodeRole: b'node' }

	
app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
ctx = engine.rootContext()
#view = QQuickView()
#ctx = view.rootContext()
model = SampleModel()
ctx.setContextProperty("myModel", model)
engine.load("test4-nested-listview.qml")
#view.setSource(QUrl("test4.qml"))
#view.show()
engine.quit.connect(app.quit)
sys.exit(app.exec_())