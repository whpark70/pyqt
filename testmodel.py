import sys
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt
from PyQt5.QtWidgets import QTableView, QListView, QTreeView, QApplication

class TestModel(QAbstractItemModel):
	def __init__(self):
		super().__init__()
		self.nodes = [ 'node-0', 'node-1', 'node-2']

	def columnCount(self, qm_index):
		return 1

	def rowCount(self, qm_index):
		return len(self.nodes)

	def parent(self, qm_index):
		return QModelIndex()		# root node

	def index(self, row, col, qm_index):
		
		if not qm_index.isValid():
			parent = self.nodes
			return QAbstractItemModel.createIndex(self, row, col, parent)
		#else:
		#	parent = qm_index.internalPointer()
		
		return QModelIndex()

	def data(self, qm_index, role):
		if not qm_index.isValid():
			return None

		if role == Qt.DisplayRole:
			return self.nodes[qm_index.row()]
		return None


app = QApplication(sys.argv)
view = QListView()
model = TestModel()
view.setModel(model)
view.show()
sys.exit(app.exec_())

