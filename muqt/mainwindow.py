# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'muqt.ui'
#
# Created: Thu Jul  2 16:15:19 2009
#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 666)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.MainNotebook = QtGui.QTabWidget(self.splitter)
        self.MainNotebook.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.MainNotebook.sizePolicy().hasHeightForWidth())
        self.MainNotebook.setSizePolicy(sizePolicy)
        self.MainNotebook.setMinimumSize(QtCore.QSize(300, 200))
        self.MainNotebook.setBaseSize(QtCore.QSize(0, 400))
        self.MainNotebook.setObjectName("MainNotebook")
        self.ChatRoomsLabel = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChatRoomsLabel.sizePolicy().hasHeightForWidth())
        self.ChatRoomsLabel.setSizePolicy(sizePolicy)
        self.ChatRoomsLabel.setObjectName("ChatRoomsLabel")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.ChatRoomsLabel)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.MainNotebook.addTab(self.ChatRoomsLabel, "")
        self.PrivateChatLabel = QtGui.QWidget()
        self.PrivateChatLabel.setObjectName("PrivateChatLabel")
        self.MainNotebook.addTab(self.PrivateChatLabel, "")
        self.logWindow = QtGui.QTextBrowser(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logWindow.sizePolicy().hasHeightForWidth())
        self.logWindow.setSizePolicy(sizePolicy)
        self.logWindow.setMinimumSize(QtCore.QSize(30, 50))
        self.logWindow.setObjectName("logWindow")
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuModes = QtGui.QMenu(self.menubar)
        self.menuModes.setEnabled(False)
        self.menuModes.setObjectName("menuModes")
        self.menuScripts = QtGui.QMenu(self.menubar)
        self.menuScripts.setEnabled(False)
        self.menuScripts.setObjectName("menuScripts")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect_to_daemon = QtGui.QAction(MainWindow)
        self.actionConnect_to_daemon.setEnabled(False)
        self.actionConnect_to_daemon.setObjectName("actionConnect_to_daemon")
        self.actionDisconnect_from_daemon = QtGui.QAction(MainWindow)
        self.actionDisconnect_from_daemon.setEnabled(False)
        self.actionDisconnect_from_daemon.setObjectName("actionDisconnect_from_daemon")
        self.actionToggle_Away = QtGui.QAction(MainWindow)
        self.actionToggle_Away.setEnabled(True)
        self.actionToggle_Away.setObjectName("actionToggle_Away")
        self.actionCheck_my_privileges = QtGui.QAction(MainWindow)
        self.actionCheck_my_privileges.setEnabled(False)
        self.actionCheck_my_privileges.setObjectName("actionCheck_my_privileges")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCommands = QtGui.QAction(MainWindow)
        self.actionCommands.setEnabled(False)
        self.actionCommands.setObjectName("actionCommands")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setEnabled(False)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout_Museeq = QtGui.QAction(MainWindow)
        self.actionAbout_Museeq.setEnabled(False)
        self.actionAbout_Museeq.setObjectName("actionAbout_Museeq")
        self.actionConfigure = QtGui.QAction(MainWindow)
        self.actionConfigure.setEnabled(False)
        self.actionConfigure.setObjectName("actionConfigure")
        self.menuFile.addAction(self.actionConnect_to_daemon)
        self.menuFile.addAction(self.actionDisconnect_from_daemon)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionToggle_Away)
        self.menuFile.addAction(self.actionCheck_my_privileges)
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionConfigure)
        self.menuHelp.addAction(self.actionCommands)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuHelp.addAction(self.actionAbout_Museeq)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuModes.menuAction())
        self.menubar.addAction(self.menuScripts.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.MainNotebook.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MuQT", None, QtGui.QApplication.UnicodeUTF8))
        self.MainNotebook.setTabText(self.MainNotebook.indexOf(self.ChatRoomsLabel), QtGui.QApplication.translate("MainWindow", "Chat Rooms", None, QtGui.QApplication.UnicodeUTF8))
        self.MainNotebook.setTabText(self.MainNotebook.indexOf(self.PrivateChatLabel), QtGui.QApplication.translate("MainWindow", "Private Chat", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuModes.setTitle(QtGui.QApplication.translate("MainWindow", "Modes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScripts.setTitle(QtGui.QApplication.translate("MainWindow", "Scripts", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect_to_daemon.setText(QtGui.QApplication.translate("MainWindow", "Connect to daemon", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnect_from_daemon.setText(QtGui.QApplication.translate("MainWindow", "Disconnect from daemon", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggle_Away.setText(QtGui.QApplication.translate("MainWindow", "Toggle away", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_my_privileges.setText(QtGui.QApplication.translate("MainWindow", "Check my privileges", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCommands.setText(QtGui.QApplication.translate("MainWindow", "Commands", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Museeq.setText(QtGui.QApplication.translate("MainWindow", "About Muqt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure.setText(QtGui.QApplication.translate("MainWindow", "Configure", None, QtGui.QApplication.UnicodeUTF8))
