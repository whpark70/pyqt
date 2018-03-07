import sys
from PyQt5.QtWidgets import QApplication, QListView, QTreeView, QStyledItemDelegate
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext

class CustomModel(QAbstractItemModel):
	NodeRole = Qt.UserRole + 1
	def __init__(self, in_nodes):
		super().__init__()
		self._root = CustomNode(None)
		for node in in_nodes:
			self._root.addChild(node)

	def addChild(self, in_node, in_parent):
		if not in_parent or not in_parent.isValid():
			parent = self._root
		else:
			parent = in_parent.internalPointer()
		parent.addChild(in_node)

	def index(self, in_row, in_column, in_parent=None):
		if not in_parent or not in_parent.isValid():
			parent = self._root
		else:
			parent = in_parent.internalPointer()

		if not QAbstractItemModel.hasIndex(self, in_row, in_column, in_parent):
			return QModelIndex()

		child = parent.child(in_row)
		if child:
			return QAbstractItemModel.createIndex(self, in_row, in_column, child)
		else:
			return QModelIndex()

	def parent(self, in_index):
		if in_index.isValid():
			p = in_index.internalPointer().parent()
			if p:
				return QAbstractItemModel.createIndex(self, p.row(), 0, p)
		return QModelIndex()

	def columnCount(self, in_index):
		if in_index.isValid():
			return in_index.internalPointer().columnCount()
		return self._root.columnCount()

	def data(self, in_index, role=None):
		if not in_index.isValid():
			return None
		node = in_index.internalPointer()
		if role == CustomModel.NodeRole:
			#print(node.data(in_index.column()))
			return node.data(in_index.column())
		return None

	def  rowCount(self, in_index):
		if in_index.isValid():
			return in_index.internalPointer().childCount()
		return self._root.childCount()

	def roleNames(self):
		return { CustomModel.NodeRole: b'node' }


class CustomNode():
	def __init__(self, in_data):
		self._data = in_data
		if type(in_data) == tuple:
			self._data = list(in_data)
		if type(in_data) == str or not hasattr(in_data, '__getitem__'):
			self._data = [ in_data ]
		
		self._columncount = len(self._data)
		self._children = []
		self._parent = None
		self._row = 0

	def childCount(self):
		return len(self._children)

	def data(self, in_column):
		if in_column >= 0 and in_column < len(self._data):
			return self._data[in_column]

	def columnCount(self):
		return self._columncount

	def child(self, in_row):
		if in_row >=0 and in_row < self.childCount():
			return self._children[in_row]

	def parent(self):
		return self._parent

	def row(self):
		return self._row

	def addChild(self, in_child):
		in_child._parent = self
		in_child._row = len(self._children)
		self._children.append(in_child)
		self._columncount = max(in_child.columnCount(), self._columncount)

class CustomDelgate(QStyledItemDelegate):
	"""docstring for sampleItemDelgate"""
	def __init__(self):
		super().__init__()
		
	def paint(self, painter, option, index):
		data = index.data()
		model = index.model()
		painter.save()
		
		painter.drawText(option.rect, 0, data)
		painter.restore()
		


if __name__ == '__main__':
	app = QApplication(sys.argv)
	items = []
	for i in 'abc':
		items.append( CustomNode(i))
		items[-1].addChild( CustomNode(['d', 'e', 'f']))
		items[-1].addChild( CustomNode(['g', 'h', 'i']))
	
	model = CustomModel(items)
	#delegate = CustomDelgate()
	
	'''
	view = QListView()
	view = QTreeView()
	view.setModel(model)
	view.setItemDelegate(delegate)
	view.show()
	'''
	engine = QQmlApplicationEngine()
	ctx = engine.rootContext()
	
	ctx.setContextProperty("myModel", model)
	engine.load("custom_model2.qml")
	engine.quit.connect(app.quit)
	
	sys.exit(app.exec_())
