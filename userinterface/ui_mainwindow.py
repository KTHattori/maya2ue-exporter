# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maya2ue_exporter_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import shiboken2 as shiboken

import maya.OpenMayaUI as OpenMayaUI

import maya2ue.resources.rc

import maya.cmds as cmds

from .ui_menu_vertical import UIMenuVertical
from .ui_button_JPEN import UIButton_JPEN
from ..module.cleaner_kit import CleanerKit
from ..module.pivot_relocator import PivotRelocator
from ..module.unreal_exporter import UnrealExporter
from ..module.logger import Logger

class GUI(QMainWindow):
	ptr = OpenMayaUI.MQtUtil.mainWindow()
	parent = shiboken.wrapInstance(int(ptr), QWidget)
 
	def __init__(self,parent=None,name=None):
		super(GUI, self).__init__(self.parent)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(573, 862)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wdt_main = QWidget(self.centralwidget)
        self.wdt_main.setObjectName(u"wdt_main")
        sizePolicy.setHeightForWidth(self.wdt_main.sizePolicy().hasHeightForWidth())
        self.wdt_main.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.wdt_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.wdt_main)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(16777215, 123))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lbl_logo = QLabel(self.widget_2)
        self.lbl_logo.setObjectName(u"lbl_logo")
        sizePolicy.setHeightForWidth(self.lbl_logo.sizePolicy().hasHeightForWidth())
        self.lbl_logo.setSizePolicy(sizePolicy)
        self.lbl_logo.setMinimumSize(QSize(201, 105))
        self.lbl_logo.setMaximumSize(QSize(201, 105))
        self.lbl_logo.setBaseSize(QSize(804, 418))
        font = QFont()
        font.setPointSize(14)
        self.lbl_logo.setFont(font)
        self.lbl_logo.setPixmap(QPixmap(u":/root/img/common/logo.png"))
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_logo)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_2)

        self.tab_content = QTabWidget(self.wdt_main)
        self.tab_content.setObjectName(u"tab_content")

        font1 = QFont()
        font1.setFamily(u"MS UI Gothic")
        self.tab_content.setFont(font1)

        self.tab_content.setAutoFillBackground(False)
        self.tab_content.setTabPosition(QTabWidget.North)
        self.tab_content.setTabShape(QTabWidget.Rounded)


        # --- pivot relocator ---
        self.pivot_relocator = PivotRelocator()
        self.pivot_relocator.make_ui(self.tab_content)

        # --- cleaner kit ---
        self.cleaner_kit = CleanerKit()
        self.cleaner_kit.make_ui(self.tab_content)

        # --- end adding tabs ---
        self.verticalLayout.addWidget(self.tab_content)


        # --- unreal exporter ---
        self.unreal_exporter = UnrealExporter()
        exporter_ui = self.unreal_exporter.make_ui(self.wdt_main)
        self.verticalLayout.addWidget(exporter_ui)

        # --- logger ---
        self.logger = Logger()
        logger_ui = self.logger.make_ui(self.wdt_main)
        self.verticalLayout.addWidget(logger_ui)

        # --- end adding widgets ---
        self.verticalLayout_2.addWidget(self.wdt_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_content.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Maya2UE Exporter", None))
        self.lbl_logo.setText("")

    # retranslateUi

