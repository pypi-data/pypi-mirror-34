# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\programming\projects\randovania\randovania/gui\randomizer_configuration_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RandomizeWindow(object):
    def setupUi(self, RandomizeWindow):
        RandomizeWindow.setObjectName("RandomizeWindow")
        RandomizeWindow.resize(802, 387)
        self.centralWidget = QtWidgets.QWidget(RandomizeWindow)
        self.centralWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.difficultyBox = QtWidgets.QGroupBox(self.centralWidget)
        self.difficultyBox.setFlat(False)
        self.difficultyBox.setCheckable(False)
        self.difficultyBox.setObjectName("difficultyBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.difficultyBox)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.minimumDifficulty = QtWidgets.QSlider(self.difficultyBox)
        self.minimumDifficulty.setMaximum(5)
        self.minimumDifficulty.setOrientation(QtCore.Qt.Horizontal)
        self.minimumDifficulty.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.minimumDifficulty.setObjectName("minimumDifficulty")
        self.gridLayout_6.addWidget(self.minimumDifficulty, 1, 1, 1, 1)
        self.minimumDifficultyLabel = QtWidgets.QLabel(self.difficultyBox)
        self.minimumDifficultyLabel.setObjectName("minimumDifficultyLabel")
        self.gridLayout_6.addWidget(self.minimumDifficultyLabel, 1, 0, 1, 1)
        self.maximumDifficulty = QtWidgets.QSlider(self.difficultyBox)
        self.maximumDifficulty.setMinimum(0)
        self.maximumDifficulty.setMaximum(5)
        self.maximumDifficulty.setProperty("value", 3)
        self.maximumDifficulty.setOrientation(QtCore.Qt.Horizontal)
        self.maximumDifficulty.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.maximumDifficulty.setObjectName("maximumDifficulty")
        self.gridLayout_6.addWidget(self.maximumDifficulty, 2, 1, 1, 1)
        self.maximumDifficultyLabel = QtWidgets.QLabel(self.difficultyBox)
        self.maximumDifficultyLabel.setObjectName("maximumDifficultyLabel")
        self.gridLayout_6.addWidget(self.maximumDifficultyLabel, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.difficultyBox)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.difficultyBox, 2, 0, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.removeHudPopup = QtWidgets.QCheckBox(self.groupBox)
        self.removeHudPopup.setObjectName("removeHudPopup")
        self.verticalLayout.addWidget(self.removeHudPopup)
        self.outOfBounds = QtWidgets.QCheckBox(self.groupBox)
        self.outOfBounds.setEnabled(False)
        self.outOfBounds.setCheckable(True)
        self.outOfBounds.setObjectName("outOfBounds")
        self.verticalLayout.addWidget(self.outOfBounds)
        self.randomizeElevators = QtWidgets.QCheckBox(self.groupBox)
        self.randomizeElevators.setObjectName("randomizeElevators")
        self.verticalLayout.addWidget(self.randomizeElevators)
        self.removeItemLoss = QtWidgets.QCheckBox(self.groupBox)
        self.removeItemLoss.setChecked(True)
        self.removeItemLoss.setObjectName("removeItemLoss")
        self.verticalLayout.addWidget(self.removeItemLoss)
        self.gridLayout.addWidget(self.groupBox, 2, 1, 2, 1)
        self.allowedTricksBox = QtWidgets.QGroupBox(self.centralWidget)
        self.allowedTricksBox.setObjectName("allowedTricksBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.allowedTricksBox)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tricksScrollArea = QtWidgets.QScrollArea(self.allowedTricksBox)
        self.tricksScrollArea.setMinimumSize(QtCore.QSize(230, 0))
        self.tricksScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tricksScrollArea.setWidgetResizable(True)
        self.tricksScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tricksScrollArea.setObjectName("tricksScrollArea")
        self.tricksContents = QtWidgets.QWidget()
        self.tricksContents.setGeometry(QtCore.QRect(0, 0, 756, 68))
        self.tricksContents.setObjectName("tricksContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tricksContents)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tricksContentLayout = QtWidgets.QVBoxLayout()
        self.tricksContentLayout.setSpacing(6)
        self.tricksContentLayout.setObjectName("tricksContentLayout")
        self.verticalLayout_5.addLayout(self.tricksContentLayout)
        self.tricksScrollArea.setWidget(self.tricksContents)
        self.gridLayout_5.addWidget(self.tricksScrollArea, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectNoTricks = QtWidgets.QPushButton(self.allowedTricksBox)
        self.selectNoTricks.setObjectName("selectNoTricks")
        self.horizontalLayout.addWidget(self.selectNoTricks)
        self.selectAllTricks = QtWidgets.QPushButton(self.allowedTricksBox)
        self.selectAllTricks.setObjectName("selectAllTricks")
        self.horizontalLayout.addWidget(self.selectAllTricks)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.allowedTricksBox, 5, 0, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout)
        RandomizeWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(RandomizeWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menuBar.setObjectName("menuBar")
        RandomizeWindow.setMenuBar(self.menuBar)

        self.retranslateUi(RandomizeWindow)
        QtCore.QMetaObject.connectSlotsByName(RandomizeWindow)

    def retranslateUi(self, RandomizeWindow):
        _translate = QtCore.QCoreApplication.translate
        RandomizeWindow.setWindowTitle(_translate("RandomizeWindow", "Hello, world!"))
        self.difficultyBox.setTitle(_translate("RandomizeWindow", "Difficulty"))
        self.minimumDifficultyLabel.setText(_translate("RandomizeWindow", "Minimum"))
        self.maximumDifficultyLabel.setText(_translate("RandomizeWindow", "Maximum"))
        self.label.setText(_translate("RandomizeWindow", "<html><head/><body><p>Each trick usage in every room of the game is rated with a difficulty level from 1 to 5. For reference, the Grand Abyss jump is level 4.</p><p>Be careful when setting minimum difficulty to 4 or 5, and maximum difficulty to 0 or 1: these seeds are rare and will take a while to find.</p></body></html>"))
        self.removeHudPopup.setToolTip(_translate("RandomizeWindow", "The \"HUD Popup\" is the popup that appears after you collect an item"))
        self.removeHudPopup.setText(_translate("RandomizeWindow", "Remove HUD popup"))
        self.outOfBounds.setToolTip(_translate("RandomizeWindow", "Currently we have no data to allow this feature"))
        self.outOfBounds.setText(_translate("RandomizeWindow", "Require Out-of-Bounds"))
        self.randomizeElevators.setText(_translate("RandomizeWindow", "Randomize Elevators"))
        self.removeItemLoss.setToolTip(_translate("RandomizeWindow", "<html><head/><body><p>When checked, you don\'t lose your items when entering Hive Chamber B for the first time.</p><p>Seeds with this unchecked are rare and may just have many items in the beggining.</p></body></html>"))
        self.removeItemLoss.setText(_translate("RandomizeWindow", "Remove Item Loss"))
        self.allowedTricksBox.setTitle(_translate("RandomizeWindow", "Allowed Tricks"))
        self.selectNoTricks.setText(_translate("RandomizeWindow", "Deselect all"))
        self.selectAllTricks.setText(_translate("RandomizeWindow", "Select all"))

