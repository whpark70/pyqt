import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QMainWindow
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt, QObject, QStringListModel
from toolbox2 import Ui_Form

class MyWindow(Ui_Form):
	"""docstring for MyMainWindow"""
	def __init__(self, widget, parent=None):
		super().__init__()
		self.setupUi(widget)
		#self.viewList =  self.verticalLayoutWidget.findChildren(QListView)		# viewlist 

		self.serverList = ['kerp', 'kerpdb', 'gw00', 'GW2','epdmapp']
		self.networkList = ['HeadUTM','Head02UTM', 'BalanUTM', 'KaUTM' ]

		serverModel = QStringListModel()
		serverModel.setStringList(self.serverList)
		self.serverListView.setModel(serverModel)

		networkModel = QStringListModel()
		networkModel.setStringList(self.networkList)
		self.networkListView.setModel(networkModel)
				
		self.verticalLayout.setAlignment(Qt.AlignTop)
		self.serverListView.setVisible(False)
		self.networkListView.setVisible(False)
		
		self.serverListView.clicked.connect(self.selectCanvas)
		self.networkListView.clicked.connect(self.selectCanvas)
	
		self.dashboardButton.clicked.connect(self.itemToggle)
		self.serverButton.clicked.connect(self.itemToggle)
		self.networkButton.clicked.connect(self.itemToggle)

		self.stackedWidget.setCurrentIndex(0)		# first page in star


	def mouseEvent(self, event):
		print(self.toolBox.currentIndex())

	

	def itemToggle(self):
		btn = Form.sender()
		if btn.objectName() == 'dashboardButton':
			self.serverListView.setVisible(False)
			self.networkListView.setVisible(False)
			self.stackedWidget.setCurrentIndex(0)		# stacked index 0: dashboard page

		elif btn.objectName() == 'serverButton':		# page name: serverSummary
			self.serverListView.setVisible(True)
			self.networkListView.setVisible(False)
			stackedWidget = self.stackedWidget.findChild(QObject, 'serverSummary', Qt.FindDirectChildrenOnly)
			self.stackedWidget.setCurrentWidget(stackedWidget)

		elif btn.objectName() == 'networkButton':		# page name: networkSummary
			self.serverListView.setVisible(False)
			self.networkListView.setVisible(True)
			stackedWidget = self.stackedWidget.findChild(QObject, 'networkSummary', Qt.FindDirectChildrenOnly)
			self.stackedWidget.setCurrentWidget(stackedWidget)

		else:
			self.serverListView.setVisible(False)
			self.networkListView.setVisible(False)
			self.stackedWidget.setCurrentIndex(0)
		
	# index: index of listview
	def selectCanvas(self, index):
		serverName = index.data()
		stackedWidget = self.stackedWidget.findChild(QObject, serverName, Qt.FindDirectChildrenOnly)
		if stackedWidget:
			self.stackedWidget.setCurrentWidget(stackedWidget)
		else:
			self.stackedWidget.setCurrentIndex(0)
		'''
		viewIndex = self.stackedWidgetDict.get(serverName,0)
		self.stackedWidget.setCurrentIndex(viewIndex)
		'''


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    Form = QWidget()
    window = MyWindow(Form)
    Form.show()
    
    sys.exit(app.exec_())