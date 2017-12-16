# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created: Fri Jun 28 12:10:56 2013
#      by: PyQt5 UI code generator 5.0-snapshot-478d7f271b71
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
        QTime)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QLineEdit, QRadioButton, QVBoxLayout,QTreeView, QHBoxLayout, QWidget)
from PyQt5.QtGui import QStandardItemModel

from keyboard_full.WKeyboard import LineEdit
from keyboard_full.WKeyboard import WKeyboard

SUBJECT, SENDER, DATE = range(3)

def addMail(model, subject, sender, date):
    model.insertRow(0)
    model.setData(model.index(0, SUBJECT), subject)
    model.setData(model.index(0, SENDER), sender)
    model.setData(model.index(0, DATE), date)


def createMailModel(parent):
    model = QStandardItemModel(0, 3, parent)

    model.setHeaderData(SUBJECT, Qt.Horizontal, "Subject")
    model.setHeaderData(SENDER, Qt.Horizontal, "Sender")
    model.setHeaderData(DATE, Qt.Horizontal, "Date")

    addMail(model, "Happy New Year!", "Grace K. <grace@software-inc.com>",
            QDateTime(QDate(2006, 12, 31), QTime(17, 3)))
    addMail(model, "Radically new concept", "Grace K. <grace@software-inc.com>",
            QDateTime(QDate(2006, 12, 22), QTime(9, 44)))
    addMail(model, "Accounts", "pascale@nospam.com",
            QDateTime(QDate(2006, 12, 31), QTime(12, 50)))
    addMail(model, "Expenses", "Joe Bloggs <joe@bloggs.com>",
            QDateTime(QDate(2006, 12, 25), QTime(11, 39)))
    addMail(model, "Re: Expenses", "Andy <andy@nospam.com>",
            QDateTime(QDate(2007, 1, 2), QTime(16, 5)))
    addMail(model, "Re: Accounts", "Joe Bloggs <joe@bloggs.com>",
            QDateTime(QDate(2007, 1, 3), QTime(14, 18)))
    addMail(model, "Re: Accounts", "Andy <andy@nospam.com>",
            QDateTime(QDate(2007, 1, 3), QTime(14, 26)))
    addMail(model, "Sports", "Linda Smith <linda.smith@nospam.com>",
            QDateTime(QDate(2007, 1, 5), QTime(11, 33)))
    addMail(model, "AW: Sports", "Rolf Newschweinstein <rolfn@nospam.com>",
            QDateTime(QDate(2007, 1, 5), QTime(12, 0)))
    addMail(model, "RE: Sports", "Petra Schmidt <petras@nospam.com>",
            QDateTime(QDate(2007, 1, 5), QTime(12, 1)))

    return model
class Ui_Camera(object):



    def setupUi(self, Camera):
        Camera.setObjectName("Camera")
        Camera.resize(668, 422)
        self.kb = WKeyboard()
        self.centralwidget = QtWidgets.QWidget(Camera)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setObjectName("stackedWidget")
        self.viewfinderPage = QtWidgets.QWidget()
        self.viewfinderPage.setObjectName("viewfinderPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.viewfinderPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.viewfinder = QCameraViewfinder(self.viewfinderPage)
        self.viewfinder.setObjectName("viewfinder")
        self.gridLayout_5.addWidget(self.viewfinder, 0, 0, 1, 1)#row column rowSpan columnSpan
        self.stackedWidget.addWidget(self.viewfinderPage)
        self.previewPage = QtWidgets.QWidget()
        self.previewPage.setObjectName("previewPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.previewPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lastImagePreviewLabel = QtWidgets.QLabel(self.previewPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastImagePreviewLabel.sizePolicy().hasHeightForWidth())
        self.lastImagePreviewLabel.setSizePolicy(sizePolicy)
        self.lastImagePreviewLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.lastImagePreviewLabel.setText("")
        self.lastImagePreviewLabel.setObjectName("lastImagePreviewLabel")
        self.gridLayout_4.addWidget(self.lastImagePreviewLabel, 0, 0, 1, 1)
#####################################################################################
        self.groupBox = QGroupBox("Exclusive Radio Buttons")

        self.radio1 = QRadioButton("&Radio button 1")
        self.radio2 = QRadioButton("R&adio button 2")
        self.radio3 = QRadioButton("Ra&dio button 3")

        self.ed1 = LineEdit(self)
        self.kb.set_receiver(self.ed1)

        # self.ed1 = QLineEdit()
        self.ed2 = LineEdit(self)
        self.kb.set_receiver(self.ed2)

        self.ed3 = QLineEdit()
        self.ed4 = QLineEdit()
        self.ed5 = QLineEdit()
        self.ed6 = QLineEdit()
        self.ed7 = QLineEdit()
        # radio1.toggle()
        # self.radio1.clicked.connect(self.changeTitle)

        # radio2.setChecked(True)

        self.vbox = QHBoxLayout()

        self.vbox.addWidget(self.ed1)
        self.vbox.addWidget(self.ed2)
        self.vbox.addWidget(self.ed3)
        self.vbox.addWidget(self.ed4)
        self.vbox.addWidget(self.ed5)
        self.vbox.addWidget(self.ed6)
        self.vbox.addWidget(self.ed7)
        self.vbox.addStretch(1)
        self.groupBox.setLayout(self.vbox)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 3, 1)

        ###

        self.sourceView = QTreeView()
        self.sourceView.setRootIsDecorated(False)
        self.sourceView.setAlternatingRowColors(True)
        self.gridLayout_4.addWidget(self.sourceView, 4, 0, 3, 1)


        self.model = createMailModel(self.sourceView)
        self.sourceView.setModel(self.model)
        ###


        self.bt = QtWidgets.QPushButton(self.previewPage)
        self.bt.setObjectName("bt")
        self.bt.setText("bt...")
        self.gridLayout_4.addWidget(self.bt,8, 0, 1, 1)
#####################################################################################
        self.stackedWidget.addWidget(self.previewPage)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 3, 1)
        self.lockButton = QtWidgets.QPushButton(self.centralwidget)
        self.lockButton.setObjectName("lockButton")
        self.gridLayout_3.addWidget(self.lockButton, 1, 1, 1, 2)

        self.captureWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.captureWidget.setObjectName("captureWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.takeImageButton = QtWidgets.QPushButton(self.tab_2)
        self.takeImageButton.setObjectName("takeImageButton")
        self.gridLayout.addWidget(self.takeImageButton, 0, 0, 2, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 161, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.exposureCompensation = QtWidgets.QSlider(self.tab_2)
        self.exposureCompensation.setMinimum(-4)
        self.exposureCompensation.setMaximum(4)
        self.exposureCompensation.setPageStep(2)
        self.exposureCompensation.setOrientation(QtCore.Qt.Horizontal)
        self.exposureCompensation.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.exposureCompensation.setObjectName("exposureCompensation")
        self.gridLayout.addWidget(self.exposureCompensation, 3, 0, 1, 1)
        self.captureWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.recordButton = QtWidgets.QPushButton(self.tab)
        self.recordButton.setObjectName("recordButton")
        self.gridLayout_2.addWidget(self.recordButton, 0, 0, 1, 1)
        self.pauseButton = QtWidgets.QPushButton(self.tab)
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout_2.addWidget(self.pauseButton, 1, 0, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.tab)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.muteButton = QtWidgets.QPushButton(self.tab)
        self.muteButton.setCheckable(True)
        self.muteButton.setObjectName("muteButton")
        self.gridLayout_2.addWidget(self.muteButton, 4, 0, 1, 1)
        self.captureWidget.addTab(self.tab, "")
        self.gridLayout_3.addWidget(self.captureWidget, 2, 1, 1, 2)
        Camera.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Camera)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDevices = QtWidgets.QMenu(self.menubar)
        self.menuDevices.setObjectName("menuDevices")
        Camera.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Camera)
        self.statusbar.setObjectName("statusbar")
        Camera.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(Camera)
        self.actionExit.setObjectName("actionExit")
        self.actionStartCamera = QtWidgets.QAction(Camera)
        self.actionStartCamera.setObjectName("actionStartCamera")
        self.actionStopCamera = QtWidgets.QAction(Camera)
        self.actionStopCamera.setObjectName("actionStopCamera")
        self.actionSettings = QtWidgets.QAction(Camera)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionStartCamera)
        self.menuFile.addAction(self.actionStopCamera)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDevices.menuAction())

        self.retranslateUi(Camera)
        self.stackedWidget.setCurrentIndex(0)
        self.captureWidget.setCurrentIndex(0)
        self.recordButton.clicked.connect(Camera.record)
        self.stopButton.clicked.connect(Camera.stop)
        self.pauseButton.clicked.connect(Camera.pause)
        self.actionExit.triggered.connect(Camera.close)
        self.takeImageButton.clicked.connect(Camera.takeImage)
        self.lockButton.clicked.connect(Camera.toggleLock)
        self.muteButton.toggled['bool'].connect(Camera.setMuted)
        self.exposureCompensation.valueChanged['int'].connect(Camera.setExposureCompensation)
        self.actionSettings.triggered.connect(Camera.configureCaptureSettings)
        self.actionStartCamera.triggered.connect(Camera.startCamera)
        self.actionStopCamera.triggered.connect(Camera.stopCamera)
        QtCore.QMetaObject.connectSlotsByName(Camera)

    def retranslateUi(self, Camera):
        _translate = QtCore.QCoreApplication.translate
        Camera.setWindowTitle(_translate("Camera", "Camera"))
        self.lockButton.setText(_translate("Camera", "Focus"))
        self.takeImageButton.setText(_translate("Camera", "Capture Photo"))
        self.label.setText(_translate("Camera", "Exposure Compensation:"))
        self.captureWidget.setTabText(self.captureWidget.indexOf(self.tab_2), _translate("Camera", "Image"))
        self.recordButton.setText(_translate("Camera", "Record"))
        self.pauseButton.setText(_translate("Camera", "Pause"))
        self.stopButton.setText(_translate("Camera", "Stop"))
        self.muteButton.setText(_translate("Camera", "Mute"))
        self.captureWidget.setTabText(self.captureWidget.indexOf(self.tab), _translate("Camera", "Video"))
        self.menuFile.setTitle(_translate("Camera", "File"))
        self.menuDevices.setTitle(_translate("Camera", "Devices"))
        self.actionExit.setText(_translate("Camera", "Exit"))
        self.actionStartCamera.setText(_translate("Camera", "Start Camera"))
        self.actionStopCamera.setText(_translate("Camera", "Stop Camera"))
        self.actionSettings.setText(_translate("Camera", "Settings"))

from PyQt5.QtMultimediaWidgets import QCameraViewfinder
