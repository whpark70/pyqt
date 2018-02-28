import sys
from PyQt5.QtCore import QUrl, Qt, QModelIndex, QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext

class SampleModel(QStringListModel):
	NodeRole = Qt.UserRole + 1
	def __init__(self):
		super().__init__()
		self.nodes = [ 'node-1', 'node-2', 'node-3']
		self.setStringList(self.nodes)

	def data(self, index, role=Qt.DisplayRole):
		row = index.row()
		if role == SampleModel.NodeRole:
			return self.nodes[row]
	
	def roleNames(self):
		return { SampleModel.NodeRole: b'node' }
	

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	engine = QQmlApplicationEngine()
	
	ctx = engine.rootContext()
	model = SampleModel()
	ctx.setContextProperty("myModel", model)
	
	engine.load("test5.qml")

	engine.quit.connect(app.quit)
	sys.exit(app.exec_())
