# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/charlie/Documents/Python/RobotCode/PyQt-Robocode/Python-Robocode/GUI/window.ui'
#
# Created: Fri Dec 20 17:46:14 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow, initial_speed = 60):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(792, 464)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("robotImages/smallRed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setStyleSheet(_fromUtf8("background-color: rgba(206, 206, 206, 162);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMaximum(10000)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(200, 0))
        self.horizontalSlider.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.horizontalSlider.setMaximum(120)
        self.horizontalSlider.setProperty("value", initial_speed)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(True)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(200, 0))
        self.graphicsView_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.graphicsView_2.setStyleSheet(_fromUtf8("background-color: rgba(194, 194, 194, 167);"))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.horizontalLayout_3.addWidget(self.graphicsView_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuBattle = QtWidgets.QMenu(self.menubar)
        self.menuBattle.setObjectName(_fromUtf8("menuBattle"))
        self.menuRobot = QtWidgets.QMenu(self.menubar)
        self.menuRobot.setObjectName(_fromUtf8("menuRobot"))
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionNew_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_2.setObjectName(_fromUtf8("actionNew_2"))
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClass_Reference = QtWidgets.QAction(MainWindow)
        self.actionClass_Reference.setObjectName(_fromUtf8("actionClass_Reference"))
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuBattle.addAction(self.actionNew)
        self.menuRobot.addAction(self.actionNew_2)
        self.menuRobot.addAction(self.actionOpen)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionClass_Reference)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuBattle.menuAction())
        self.menubar.addAction(self.menuRobot.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Robocode", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1st", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2nd", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "3rd", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Points", None))
        self.pushButton.setText(_translate("MainWindow", "Start Last Battle", None))
        self.label_2.setText(_translate("MainWindow", "Battle\'s Number", None))
        self.label.setText(_translate("MainWindow", "Game Speed", None))
        self.menuBattle.setTitle(_translate("MainWindow", "Battle", None))
        self.menuRobot.setTitle(_translate("MainWindow", "Robot", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew_2.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionClass_Reference.setText(_translate("MainWindow", "Class Reference", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
