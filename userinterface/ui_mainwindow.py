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

from . import ui_menu_vertical
from ..module import cleaner_kit

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
        MainWindow.resize(567, 752)
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
        self.tab_pivot = QWidget()
        self.tab_pivot.setObjectName(u"tab_pivot")
        self.verticalLayout_7 = QVBoxLayout(self.tab_pivot)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.wdt_pivotLabel = QWidget(self.tab_pivot)
        self.wdt_pivotLabel.setObjectName(u"wdt_pivotLabel")
        self.wdt_pivotLabel.setMaximumSize(QSize(16777215, 46))
        font2 = QFont()
        font2.setPointSize(16)
        self.wdt_pivotLabel.setFont(font2)
        self.horizontalLayout_6 = QHBoxLayout(self.wdt_pivotLabel)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_pivotIcon = QLabel(self.wdt_pivotLabel)
        self.lbl_pivotIcon.setObjectName(u"lbl_pivotIcon")
        self.lbl_pivotIcon.setMinimumSize(QSize(28, 28))
        self.lbl_pivotIcon.setMaximumSize(QSize(28, 28))
        self.lbl_pivotIcon.setPixmap(QPixmap(u":/root/img/pivot_relocator/icon_pivot_relocator.png"))
        self.lbl_pivotIcon.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.lbl_pivotIcon)

        self.lbl_pivotLabel = QLabel(self.wdt_pivotLabel)
        self.lbl_pivotLabel.setObjectName(u"lbl_pivotLabel")
        self.lbl_pivotLabel.setFont(font2)

        self.horizontalLayout_6.addWidget(self.lbl_pivotLabel)


        self.verticalLayout_7.addWidget(self.wdt_pivotLabel)

        self.wdt_pivotFlag = QWidget(self.tab_pivot)
        self.wdt_pivotFlag.setObjectName(u"wdt_pivotFlag")
        self.horizontalLayout_2 = QHBoxLayout(self.wdt_pivotFlag)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chk_pivotFlag_All = QCheckBox(self.wdt_pivotFlag)
        self.chk_pivotFlag_All.setObjectName(u"chk_pivotFlag_All")

        self.horizontalLayout_2.addWidget(self.chk_pivotFlag_All)


        self.verticalLayout_7.addWidget(self.wdt_pivotFlag)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.wdt_pivotContent = QWidget(self.tab_pivot)
        self.wdt_pivotContent.setObjectName(u"wdt_pivotContent")
        self.horizontalLayout_3 = QHBoxLayout(self.wdt_pivotContent)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.wdt_pivot = QWidget(self.wdt_pivotContent)
        self.wdt_pivot.setObjectName(u"wdt_pivot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.wdt_pivot.sizePolicy().hasHeightForWidth())
        self.wdt_pivot.setSizePolicy(sizePolicy1)
        self.wdt_pivot.setMinimumSize(QSize(200, 200))
        self.lbl_pivotBase = QLabel(self.wdt_pivot)
        self.lbl_pivotBase.setObjectName(u"lbl_pivotBase")
        self.lbl_pivotBase.setGeometry(QRect(13, 13, 171, 171))
        self.lbl_pivotBase.setPixmap(QPixmap(u":/root/img/pivot_relocator/pivot_base.png"))
        self.lbl_pivotBase.setScaledContents(True)
        self.btn_pivotZmin = QPushButton(self.wdt_pivot)
        self.btn_pivotZmin.setObjectName(u"btn_pivotZmin")
        self.btn_pivotZmin.setGeometry(QRect(150, 40, 36, 36))
        self.btn_pivotZmin.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/root/img/pivot_relocator/pivot_minZ.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pivotZmin.setIcon(icon)
        self.btn_pivotZmin.setIconSize(QSize(24, 24))
        self.btn_pivotZmin.setAutoDefault(False)
        self.btn_pivotZmin.setFlat(True)
        self.btn_pivotZmax = QPushButton(self.wdt_pivot)
        self.btn_pivotZmax.setObjectName(u"btn_pivotZmax")
        self.btn_pivotZmax.setGeometry(QRect(10, 120, 36, 36))
        self.btn_pivotZmax.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/root/img/pivot_relocator/pivot_maxZ.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pivotZmax.setIcon(icon1)
        self.btn_pivotZmax.setIconSize(QSize(24, 24))
        self.btn_pivotZmax.setAutoDefault(False)
        self.btn_pivotZmax.setFlat(True)
        self.btn_pivotYmax = QPushButton(self.wdt_pivot)
        self.btn_pivotYmax.setObjectName(u"btn_pivotYmax")
        self.btn_pivotYmax.setGeometry(QRect(80, 0, 36, 36))
        self.btn_pivotYmax.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/root/img/pivot_relocator/pivot_maxY.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pivotYmax.setIcon(icon2)
        self.btn_pivotYmax.setIconSize(QSize(24, 24))
        self.btn_pivotYmax.setAutoDefault(False)
        self.btn_pivotYmax.setFlat(True)
        self.btn_pivotXmin = QPushButton(self.wdt_pivot)
        self.btn_pivotXmin.setObjectName(u"btn_pivotXmin")
        self.btn_pivotXmin.setGeometry(QRect(0, 80, 36, 36))
        self.btn_pivotXmin.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/root/img/pivot_relocator/pivot_minX.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pivotXmin.setIcon(icon3)
        self.btn_pivotXmin.setIconSize(QSize(24, 24))
        self.btn_pivotXmin.setAutoDefault(False)
        self.btn_pivotXmin.setFlat(True)
        self.btn_pivotYmin = QPushButton(self.wdt_pivot)
        self.btn_pivotYmin.setObjectName(u"btn_pivotYmin")
        self.btn_pivotYmin.setGeometry(QRect(80, 160, 36, 36))
        self.btn_pivotYmin.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/root/img/pivot_relocator/pivot_minY.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pivotYmin.setIcon(icon4)
        self.btn_pivotYmin.setIconSize(QSize(24, 24))
        self.btn_pivotYmin.setAutoDefault(False)
        self.btn_pivotYmin.setFlat(True)
        self.btn_pivotXmax = QPushButton(self.wdt_pivot)
        self.btn_pivotXmax.setObjectName(u"btn_pivotXmax")
        self.btn_pivotXmax.setGeometry(QRect(160, 80, 36, 36))
        self.btn_pivotXmax.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/root/img/pivot_relocator/pivot_maxX.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pivotXmax.setIcon(icon5)
        self.btn_pivotXmax.setIconSize(QSize(24, 24))
        self.btn_pivotXmax.setAutoDefault(False)
        self.btn_pivotXmax.setFlat(True)
        self.btn_pivotCenter = QPushButton(self.wdt_pivot)
        self.btn_pivotCenter.setObjectName(u"btn_pivotCenter")
        self.btn_pivotCenter.setGeometry(QRect(70, 70, 54, 54))
        self.btn_pivotCenter.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/root/img/pivot_relocator/pivot_zero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pivotCenter.setIcon(icon6)
        self.btn_pivotCenter.setIconSize(QSize(40, 40))
        self.btn_pivotCenter.setAutoDefault(False)
        self.btn_pivotCenter.setFlat(True)

        self.horizontalLayout_3.addWidget(self.wdt_pivot)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addWidget(self.wdt_pivotContent)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.lbl_pivotLog = QLabel(self.tab_pivot)
        self.lbl_pivotLog.setObjectName(u"lbl_pivotLog")
        self.lbl_pivotLog.setTextFormat(Qt.AutoText)
        self.lbl_pivotLog.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.lbl_pivotLog)

        icon7 = QIcon()
        icon7.addFile(u":/root/img/pivot_relocator/icon_pivot_relocator.png", QSize(), QIcon.Normal, QIcon.Off)



        # cleaner
        self.tab_content.addTab(self.tab_pivot, icon7, "")
        self.tab_clean = QWidget()
        self.tab_clean.setObjectName(u"tab_clean")
        self.verticalLayout_3 = QVBoxLayout(self.tab_clean)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.wdt_cleanerLabel = QWidget(self.tab_clean)
        self.wdt_cleanerLabel.setObjectName(u"wdt_cleanerLabel")
        self.wdt_cleanerLabel.setMaximumSize(QSize(16777215, 46))
        self.wdt_cleanerLabel.setFont(font2)
        self.horizontalLayout_7 = QHBoxLayout(self.wdt_cleanerLabel)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_cleanerIcon = QLabel(self.wdt_cleanerLabel)
        self.lbl_cleanerIcon.setObjectName(u"lbl_cleanerIcon")
        self.lbl_cleanerIcon.setMinimumSize(QSize(28, 28))
        self.lbl_cleanerIcon.setMaximumSize(QSize(28, 28))
        self.lbl_cleanerIcon.setPixmap(QPixmap(u":/root/img/cleaner_kit/icon_cleaner_kit.png"))
        self.lbl_cleanerIcon.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.lbl_cleanerIcon)

        self.lbl_cleanerLabel = QLabel(self.wdt_cleanerLabel)
        self.lbl_cleanerLabel.setObjectName(u"lbl_cleanerLabel")
        self.lbl_cleanerLabel.setFont(font2)

        self.horizontalLayout_7.addWidget(self.lbl_cleanerLabel)


        self.verticalLayout_3.addWidget(self.wdt_cleanerLabel)

        self.cleanerMenu = ui_menu_vertical.UIMenuVertical("cleaner")
        self.wdt_cleanerContent = self.cleanerMenu.construct(self.tab_clean)
        self.cleanerMenu.create_button("Delete All History", lambda: cleaner_kit.freeze_transform())
        self.cleanerMenu.create_button("Freeze Transform", lambda: cleaner_kit.freeze_transform())
        self.cleanerMenu.create_button("Print Debug", lambda: cleaner_kit.print_debug())

        self.verticalLayout_3.addWidget(self.wdt_cleanerContent)

        icon8 = QIcon()
        icon8.addFile(u":/root/img/cleaner_kit/icon_cleaner_kit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_content.addTab(self.tab_clean, icon8, "")

        self.verticalLayout.addWidget(self.tab_content)

        self.frm_export = QFrame(self.wdt_main)
        self.frm_export.setObjectName(u"frm_export")
        font3 = QFont()
        font3.setFamily(u"\u6e90\u668e\u30a8\u30e0\u30b4v2 Bold")
        self.frm_export.setFont(font3)
        self.frm_export.setFrameShape(QFrame.StyledPanel)
        self.frm_export.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frm_export)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.wdt_export = QGroupBox(self.frm_export)
        self.wdt_export.setObjectName(u"wdt_export")
        self.wdt_export.setFont(font1)
        self.wdt_export.setAlignment(Qt.AlignCenter)
        self.wdt_export.setFlat(True)
        self.wdt_export.setCheckable(False)
        self.verticalLayout_8 = QVBoxLayout(self.wdt_export)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cbx_exporttype = QComboBox(self.wdt_export)
        self.cbx_exporttype.addItem("")
        self.cbx_exporttype.addItem("")
        self.cbx_exporttype.addItem("")
        self.cbx_exporttype.setObjectName(u"cbx_exporttype")
        font4 = QFont()
        font4.setPointSize(12)
        self.cbx_exporttype.setFont(font4)

        self.verticalLayout_8.addWidget(self.cbx_exporttype)

        self.wdt_rename = QWidget(self.wdt_export)
        self.wdt_rename.setObjectName(u"wdt_rename")
        self.horizontalLayout = QHBoxLayout(self.wdt_rename)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.wdt_pref_input = QWidget(self.wdt_rename)
        self.wdt_pref_input.setObjectName(u"wdt_pref_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.wdt_pref_input.sizePolicy().hasHeightForWidth())
        self.wdt_pref_input.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.wdt_pref_input)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_pref_input = QLabel(self.wdt_pref_input)
        self.lbl_pref_input.setObjectName(u"lbl_pref_input")

        self.verticalLayout_4.addWidget(self.lbl_pref_input)

        self.led_pref_input = QLineEdit(self.wdt_pref_input)
        self.led_pref_input.setObjectName(u"led_pref_input")

        self.verticalLayout_4.addWidget(self.led_pref_input)


        self.horizontalLayout.addWidget(self.wdt_pref_input)

        self.wdt_body_input = QWidget(self.wdt_rename)
        self.wdt_body_input.setObjectName(u"wdt_body_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.wdt_body_input.sizePolicy().hasHeightForWidth())
        self.wdt_body_input.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.wdt_body_input)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_body_input = QLabel(self.wdt_body_input)
        self.lbl_body_input.setObjectName(u"lbl_body_input")

        self.verticalLayout_5.addWidget(self.lbl_body_input)

        self.led_body_input = QLineEdit(self.wdt_body_input)
        self.led_body_input.setObjectName(u"led_body_input")

        self.verticalLayout_5.addWidget(self.led_body_input)


        self.horizontalLayout.addWidget(self.wdt_body_input)

        self.pushButton = QPushButton(self.wdt_rename)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_8.addWidget(self.wdt_rename)


        self.verticalLayout_6.addWidget(self.wdt_export)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.frm_export)


        self.verticalLayout_2.addWidget(self.wdt_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab_content.setCurrentIndex(0)
        self.btn_pivotZmin.setDefault(False)
        self.btn_pivotZmax.setDefault(False)
        self.btn_pivotYmax.setDefault(False)
        self.btn_pivotXmin.setDefault(False)
        self.btn_pivotYmin.setDefault(False)
        self.btn_pivotXmax.setDefault(False)
        self.btn_pivotCenter.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Maya2UE Exporter", None))
        self.lbl_logo.setText("")
        self.lbl_pivotIcon.setText("")
        self.lbl_pivotLabel.setText(QCoreApplication.translate("MainWindow", u"Pivot Relocator", None))
        self.chk_pivotFlag_All.setText(QCoreApplication.translate("MainWindow", u"\u9078\u629e\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u5168\u3066\u306e\u5883\u754c\u3092\u8003\u616e\u3059\u308b - Apply boundary box on all selected", None))
        self.lbl_pivotBase.setText("")
        self.btn_pivotZmin.setText("")
        self.btn_pivotZmax.setText("")
        self.btn_pivotYmax.setText("")
        self.btn_pivotXmin.setText("")
        self.btn_pivotYmin.setText("")
        self.btn_pivotXmax.setText("")
        self.btn_pivotCenter.setText("")
        self.lbl_pivotLog.setText("")
        self.tab_content.setTabText(self.tab_content.indexOf(self.tab_pivot), QCoreApplication.translate("MainWindow", u"Pivot", None))
        self.lbl_cleanerIcon.setText("")
        self.lbl_cleanerLabel.setText(QCoreApplication.translate("MainWindow", u"Cleaner Kit", None))
        self.tab_content.setTabText(self.tab_content.indexOf(self.tab_clean), QCoreApplication.translate("MainWindow", u"Clean", None))
        self.wdt_export.setTitle(QCoreApplication.translate("MainWindow", u" Export ", None))
        self.cbx_exporttype.setItemText(0, QCoreApplication.translate("MainWindow", u"Meshes Only (Static Mesh)", None))
        self.cbx_exporttype.setItemText(1, QCoreApplication.translate("MainWindow", u"Bones Only (Skeleton)", None))
        self.cbx_exporttype.setItemText(2, QCoreApplication.translate("MainWindow", u"Meshes + Bones (Skeletal Mesh)", None))

        self.lbl_pref_input.setText(QCoreApplication.translate("MainWindow", u"Prefix", None))
        self.lbl_body_input.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Export\n"
"\u30a8\u30af\u30b9\u30dd\u30fc\u30c8", None))
    # retranslateUi

