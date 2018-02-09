import sys
import types
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QHBoxLayout
from PyQt5.QtGui import QStandardItem, QStandardItemModel

class MainFrame(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		nested_list = { 
			"1": ["A", "B", "C"],
			"2": ["C", "D", "E"]
		}

		self.tree = QTreeView(self)
		layout = QHBoxLayout(self)
		layout.addWidget(self.tree)

		model = QStandardItemModel()
		self.tree.setModel(model)
		self.displayTree( nested_list, model.invisibleRootItem())

	def displayTree(self, children, parent):
		for child in sorted(children):
			child_item = QStandardItem(child)
			parent.appendRow(child_item)
			if type(children) ==dict:
				self.displayTree(children(child), child_item)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = MainFrame()
	main.show()
	sys.exit(app.exec_())