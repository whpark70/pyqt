# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolbox2_expand.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setStyleSheet("QWidget {\n"
"    background-color: white\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(400, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboardButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboardButton.sizePolicy().hasHeightForWidth())
        self.dashboardButton.setSizePolicy(sizePolicy)
        self.dashboardButton.setMinimumSize(QtCore.QSize(250, 0))
        self.dashboardButton.setObjectName("dashboardButton")
        self.verticalLayout.addWidget(self.dashboardButton)
        self.serverButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverButton.sizePolicy().hasHeightForWidth())
        self.serverButton.setSizePolicy(sizePolicy)
        self.serverButton.setMinimumSize(QtCore.QSize(250, 0))
        self.serverButton.setObjectName("serverButton")
        self.verticalLayout.addWidget(self.serverButton)
        self.serverListView = MyList(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverListView.sizePolicy().hasHeightForWidth())
        self.serverListView.setSizePolicy(sizePolicy)
        self.serverListView.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.serverListView.setFont(font)
        self.serverListView.setStyleSheet("")
        self.serverListView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.serverListView.setResizeMode(QtWidgets.QListView.Adjust)
        self.serverListView.setUniformItemSizes(False)
        self.serverListView.setObjectName("serverListView")
        self.verticalLayout.addWidget(self.serverListView)
        self.networkButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.networkButton.sizePolicy().hasHeightForWidth())
        self.networkButton.setSizePolicy(sizePolicy)
        self.networkButton.setMinimumSize(QtCore.QSize(250, 0))
        self.networkButton.setObjectName("networkButton")
        self.verticalLayout.addWidget(self.networkButton)
        self.networkListView = MyList(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.networkListView.sizePolicy().hasHeightForWidth())
        self.networkListView.setSizePolicy(sizePolicy)
        self.networkListView.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.networkListView.setFont(font)
        self.networkListView.setObjectName("networkListView")
        self.verticalLayout.addWidget(self.networkListView)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("QStackedWidget {\n"
"    border: 1px solid lightgray;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboard = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.dashboard.setFont(font)
        self.dashboard.setObjectName("dashboard")
        self.label_3 = QtWidgets.QLabel(self.dashboard)
        self.label_3.setGeometry(QtCore.QRect(320, 210, 201, 71))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.dashboard)
        self.serverSummary = QtWidgets.QWidget()
        self.serverSummary.setObjectName("serverSummary")
        self.label_4 = QtWidgets.QLabel(self.serverSummary)
        self.label_4.setGeometry(QtCore.QRect(260, 210, 341, 71))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.serverSummary)
        self.kerp = QtWidgets.QWidget()
        self.kerp.setObjectName("kerp")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.kerp)
        self.gridLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.kerpTopLayout = QtWidgets.QHBoxLayout()
        self.kerpTopLayout.setObjectName("kerpTopLayout")
        self.gridLayout_2.addLayout(self.kerpTopLayout, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.kerp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel { background-color:  #e0f7fa  }")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.kerpInfo = QtWidgets.QTextBrowser(self.kerp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kerpInfo.sizePolicy().hasHeightForWidth())
        self.kerpInfo.setSizePolicy(sizePolicy)
        self.kerpInfo.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.kerpInfo.setFont(font)
        self.kerpInfo.setObjectName("kerpInfo")
        self.gridLayout_2.addWidget(self.kerpInfo, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.kerp)
        self.kerpdb = QtWidgets.QWidget()
        self.kerpdb.setObjectName("kerpdb")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.kerpdb)
        self.gridLayout_4.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.kerpdbTopLayout = QtWidgets.QHBoxLayout()
        self.kerpdbTopLayout.setObjectName("kerpdbTopLayout")
        self.gridLayout_4.addLayout(self.kerpdbTopLayout, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.kerpdb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.kerpdbInfo = QtWidgets.QTextBrowser(self.kerpdb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kerpdbInfo.sizePolicy().hasHeightForWidth())
        self.kerpdbInfo.setSizePolicy(sizePolicy)
        self.kerpdbInfo.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.kerpdbInfo.setFont(font)
        self.kerpdbInfo.setObjectName("kerpdbInfo")
        self.gridLayout_4.addWidget(self.kerpdbInfo, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.kerpdb)
        self.gw00 = QtWidgets.QWidget()
        self.gw00.setObjectName("gw00")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gw00)
        self.gridLayout_5.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_5.setVerticalSpacing(3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gw00TopLayout = QtWidgets.QHBoxLayout()
        self.gw00TopLayout.setSpacing(0)
        self.gw00TopLayout.setObjectName("gw00TopLayout")
        self.gridLayout_5.addLayout(self.gw00TopLayout, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gw00)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.gw00Info = QtWidgets.QTextBrowser(self.gw00)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gw00Info.sizePolicy().hasHeightForWidth())
        self.gw00Info.setSizePolicy(sizePolicy)
        self.gw00Info.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.gw00Info.setFont(font)
        self.gw00Info.setObjectName("gw00Info")
        self.gridLayout_5.addWidget(self.gw00Info, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.gw00)
        self.GW2 = QtWidgets.QWidget()
        self.GW2.setObjectName("GW2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.GW2)
        self.gridLayout_6.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_6.setVerticalSpacing(3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.GW2TopLayout = QtWidgets.QHBoxLayout()
        self.GW2TopLayout.setSpacing(0)
        self.GW2TopLayout.setObjectName("GW2TopLayout")
        self.gridLayout_6.addLayout(self.GW2TopLayout, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.GW2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.GW2Info = QtWidgets.QTextBrowser(self.GW2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GW2Info.sizePolicy().hasHeightForWidth())
        self.GW2Info.setSizePolicy(sizePolicy)
        self.GW2Info.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.GW2Info.setFont(font)
        self.GW2Info.setObjectName("GW2Info")
        self.gridLayout_6.addWidget(self.GW2Info, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.GW2)
        self.epdmapp = QtWidgets.QWidget()
        self.epdmapp.setObjectName("epdmapp")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.epdmapp)
        self.gridLayout_7.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_7.setVerticalSpacing(3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.epdmapp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.epdmappTopLayout = QtWidgets.QHBoxLayout()
        self.epdmappTopLayout.setSpacing(0)
        self.epdmappTopLayout.setObjectName("epdmappTopLayout")
        self.gridLayout_7.addLayout(self.epdmappTopLayout, 1, 0, 1, 1)
        self.epdmappInfo = QtWidgets.QTextBrowser(self.epdmapp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.epdmappInfo.sizePolicy().hasHeightForWidth())
        self.epdmappInfo.setSizePolicy(sizePolicy)
        self.epdmappInfo.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.epdmappInfo.setFont(font)
        self.epdmappInfo.setObjectName("epdmappInfo")
        self.gridLayout_7.addWidget(self.epdmappInfo, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.epdmapp)
        self.epdmfms = QtWidgets.QWidget()
        self.epdmfms.setObjectName("epdmfms")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.epdmfms)
        self.gridLayout_8.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_8.setVerticalSpacing(3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.epdmfmsTopLayout = QtWidgets.QHBoxLayout()
        self.epdmfmsTopLayout.setSpacing(0)
        self.epdmfmsTopLayout.setObjectName("epdmfmsTopLayout")
        self.gridLayout_8.addLayout(self.epdmfmsTopLayout, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.epdmfms)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        self.epdmfmsInfo = QtWidgets.QTextBrowser(self.epdmfms)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.epdmfmsInfo.sizePolicy().hasHeightForWidth())
        self.epdmfmsInfo.setSizePolicy(sizePolicy)
        self.epdmfmsInfo.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.epdmfmsInfo.setFont(font)
        self.epdmfmsInfo.setObjectName("epdmfmsInfo")
        self.gridLayout_8.addWidget(self.epdmfmsInfo, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.epdmfms)
        self.bi = QtWidgets.QWidget()
        self.bi.setObjectName("bi")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.bi)
        self.gridLayout_9.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_9.setVerticalSpacing(3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_11 = QtWidgets.QLabel(self.bi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 1)
        self.biTopLayout = QtWidgets.QHBoxLayout()
        self.biTopLayout.setSpacing(0)
        self.biTopLayout.setObjectName("biTopLayout")
        self.gridLayout_9.addLayout(self.biTopLayout, 1, 0, 1, 1)
        self.biInfo = QtWidgets.QTextBrowser(self.bi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.biInfo.sizePolicy().hasHeightForWidth())
        self.biInfo.setSizePolicy(sizePolicy)
        self.biInfo.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.biInfo.setFont(font)
        self.biInfo.setObjectName("biInfo")
        self.gridLayout_9.addWidget(self.biInfo, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.bi)
        self.kerpholdings = QtWidgets.QWidget()
        self.kerpholdings.setObjectName("kerpholdings")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.kerpholdings)
        self.gridLayout_10.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_10.setVerticalSpacing(3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.kerpholdingsTopLayout = QtWidgets.QHBoxLayout()
        self.kerpholdingsTopLayout.setSpacing(0)
        self.kerpholdingsTopLayout.setObjectName("kerpholdingsTopLayout")
        self.gridLayout_10.addLayout(self.kerpholdingsTopLayout, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.kerpholdings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 0, 0, 1, 1)
        self.kerpholdingsInfo = QtWidgets.QTextBrowser(self.kerpholdings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kerpholdingsInfo.sizePolicy().hasHeightForWidth())
        self.kerpholdingsInfo.setSizePolicy(sizePolicy)
        self.kerpholdingsInfo.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.kerpholdingsInfo.setFont(font)
        self.kerpholdingsInfo.setObjectName("kerpholdingsInfo")
        self.gridLayout_10.addWidget(self.kerpholdingsInfo, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.kerpholdings)
        self.kerpholdingsDB = QtWidgets.QWidget()
        self.kerpholdingsDB.setObjectName("kerpholdingsDB")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.kerpholdingsDB)
        self.gridLayout_11.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_11.setVerticalSpacing(3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.kerpholdingsDBTopLayout = QtWidgets.QHBoxLayout()
        self.kerpholdingsDBTopLayout.setSpacing(0)
        self.kerpholdingsDBTopLayout.setObjectName("kerpholdingsDBTopLayout")
        self.gridLayout_11.addLayout(self.kerpholdingsDBTopLayout, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.kerpholdingsDB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_11.addWidget(self.label_13, 0, 0, 1, 1)
        self.kerpholdingsDBInfo = QtWidgets.QTextBrowser(self.kerpholdingsDB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kerpholdingsDBInfo.sizePolicy().hasHeightForWidth())
        self.kerpholdingsDBInfo.setSizePolicy(sizePolicy)
        self.kerpholdingsDBInfo.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.kerpholdingsDBInfo.setFont(font)
        self.kerpholdingsDBInfo.setObjectName("kerpholdingsDBInfo")
        self.gridLayout_11.addWidget(self.kerpholdingsDBInfo, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.kerpholdingsDB)
        self.networkSummary = QtWidgets.QWidget()
        self.networkSummary.setObjectName("networkSummary")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.networkSummary)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.networkSummary)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.networkSummary)
        self.HeadUTM = QtWidgets.QWidget()
        self.HeadUTM.setObjectName("HeadUTM")
        self.label_6 = QtWidgets.QLabel(self.HeadUTM)
        self.label_6.setGeometry(QtCore.QRect(290, 240, 361, 71))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.HeadUTM)
        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AP시스템 모니터링"))
        self.dashboardButton.setText(_translate("Form", "대시보드"))
        self.serverButton.setText(_translate("Form", "서     버"))
        self.networkButton.setText(_translate("Form", "네트워크"))
        self.label_3.setText(_translate("Form", "Dashboard"))
        self.label_4.setText(_translate("Form", "Server Summary"))
        self.label.setText(_translate("Form", "KERP"))
        self.label_2.setText(_translate("Form", "KERPDB"))
        self.label_7.setText(_translate("Form", "그룹웨어"))
        self.label_8.setText(_translate("Form", "그룹웨어DB"))
        self.label_9.setText(_translate("Form", "EPDM APP"))
        self.label_10.setText(_translate("Form", "EPDM FMS"))
        self.label_11.setText(_translate("Form", "BI"))
        self.label_12.setText(_translate("Form", "홀딩스 ERP"))
        self.label_13.setText(_translate("Form", "홀딩스 ERP DB"))
        self.label_5.setText(_translate("Form", "Network Summary"))
        self.label_6.setText(_translate("Form", "AP 본사 UTM"))

from customWidget import MyList
