import sys
from PyQt5.QtCore import QUrl, Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext

class SampleModel(QStandardItemModel):
	NodeRole = Qt.UserRole + 1
	def __init__(self):
		super().__init__()
		self.nodes = [ 'node-1', 'node-2', 'node-3']

		for node in self.nodes:
			item = QStandardItem(node)
			self.appendRow(item)

	def rowCount(self, parent=QModelIndex):
		return len(self.nodes)

	def data(self, index, role=Qt.DisplayRole):
		row = index.row()
		if role == SampleModel.NodeRole:
			return self.nodes[row]

	def roleNames(self):
		return { SampleModel.NodeRole: b'node' }

	
app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
ctx = engine.rootContext()
#view = QQuickView()
#ctx = view.rootContext()
model = SampleModel()
ctx.setContextProperty("myModel", model)
engine.load("test4-listview.qml")
#view.setSource(QUrl("test4.qml"))
#view.show()
engine.quit.connect(app.quit)
sys.exit(app.exec_())