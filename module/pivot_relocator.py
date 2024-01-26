# pivot relocator module for maya2ue exporter

import maya.cmds as cmds
from enum import Enum
from .module_base import ModuleBase
from ..userinterface.ui_button_icon import UIButtonIcon
from ..userinterface.ui_button_JPEN import UIButton_JPEN

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# class definition of pivot relocator
class PivotRelocator(ModuleBase):
    class RelocateType(Enum):
        Min_X = 0
        Min_Y = 1
        Min_Z = 2
        Max_X = 3
        Max_Y = 4
        Max_Z = 5
        Center = 6

    def __init__(self):
        super().__init__("Pivot Relocator")

    def initialize(self):
        pass

    def construct_ui(self, parentUI = None):
        self.tab_pivot = QWidget()
        self.tab_pivot.setObjectName(u"tab_pivot")
        self.verticalLayout_7 = QVBoxLayout(self.tab_pivot)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.wdt_pivotLabel = QWidget(self.tab_pivot)
        self.wdt_pivotLabel.setObjectName(u"wdt_pivotLabel")
        self.wdt_pivotLabel.setMaximumSize(QSize(16777215, 46))

        font_label = QFont()
        font_label.setPointSize(16)
        font_label.setBold(True)

        font_content = QFont()
        font_content.setPointSize(16)
        font_content.setBold(True)
        
        self.wdt_pivotLabel.setFont(font_label)
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
        self.lbl_pivotLabel.setFont(font_content)

        self.horizontalLayout_6.addWidget(self.lbl_pivotLabel)


        self.verticalLayout_7.addWidget(self.wdt_pivotLabel)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.gbox_pivotContent = QGroupBox(self.tab_pivot)
        self.gbox_pivotContent.setFlat(True)
        self.gbox_pivotContent.setCheckable(False)
        self.gbox_pivotContent.setObjectName(u"gbox_pivotContent")
        self.gbox_pivotContent.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3 = QHBoxLayout(self.gbox_pivotContent)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.wdt_pivot = QWidget(self.gbox_pivotContent)
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

        # create buttons
        iconsize = 24
        iconpath_root = ":/root/img/pivot_relocator/"

        # Z axis
        btn_pivotZmin = UIButtonIcon("pivotZmin")
        btn_pivotZmin.set_icon(QIcon(iconpath_root + "pivot_minZ.png"))
        btn_pivotZmin.set_icon_size(iconsize)
        btn_pivotZmin.set_flat(True)
        btn_pivotZmin.bind_function_on_clicked(lambda: self.relocate_pivot(PivotRelocator.RelocateType.Min_Z))
        btn_pivotZmin.construct(self.wdt_pivot)
        self.btn_pivotZmin = btn_pivotZmin.component
        self.btn_pivotZmin.setGeometry(QRect(150, 40, 36, 36))
        self.btn_pivotZmin.setAutoFillBackground(False)

        btn_pivotZmax = UIButtonIcon("pivotZmax")
        btn_pivotZmax.set_icon(QIcon(iconpath_root + "pivot_maxZ.png"))
        btn_pivotZmax.set_icon_size(iconsize)
        btn_pivotZmax.set_flat(True)
        btn_pivotZmax.bind_function_on_clicked(lambda: self.relocate_pivot(PivotRelocator.RelocateType.Max_Z))
        btn_pivotZmax.construct(self.wdt_pivot)
        self.btn_pivotZmax = btn_pivotZmax.component
        self.btn_pivotZmax.setGeometry(QRect(10, 120, 36, 36))
        self.btn_pivotZmax.setAutoFillBackground(False)

        # Y axis
        btn_pivotYmin = UIButtonIcon("pivotYmin")
        btn_pivotYmin.set_icon(QIcon(iconpath_root + "pivot_minY.png"))
        btn_pivotYmin.set_icon_size(iconsize)
        btn_pivotYmin.set_flat(True)
        btn_pivotYmin.bind_function_on_clicked(lambda: self.relocate_pivot(PivotRelocator.RelocateType.Min_Y))
        btn_pivotYmin.construct(self.wdt_pivot)
        self.btn_pivotYmin = btn_pivotYmin.component
        self.btn_pivotYmin.setGeometry(QRect(80, 160, 36, 36))
        self.btn_pivotYmin.setAutoFillBackground(False)

        btn_pivotYmax = UIButtonIcon("pivotYmax")
        btn_pivotYmax.set_icon(QIcon(iconpath_root + "pivot_maxY.png"))
        btn_pivotYmax.set_icon_size(iconsize)
        btn_pivotYmax.set_flat(True)
        btn_pivotYmax.bind_function_on_clicked(lambda: self.relocate_pivot(PivotRelocator.RelocateType.Max_Y))
        btn_pivotYmax.construct(self.wdt_pivot)
        self.btn_pivotYmax = btn_pivotYmax.component
        self.btn_pivotYmax.setGeometry(QRect(80, 0, 36, 36))
        self.btn_pivotYmax.setAutoFillBackground(False)

        # X axis
        btn_pivotXmin = UIButtonIcon("pivotXmin")
        btn_pivotXmin.set_icon(QIcon(iconpath_root + "pivot_minX.png"))
        btn_pivotXmin.set_icon_size(iconsize)
        btn_pivotXmin.set_flat(True)
        btn_pivotXmin.bind_function_on_clicked(lambda: self.relocate_pivot(PivotRelocator.RelocateType.Min_X))
        btn_pivotXmin.construct(self.wdt_pivot)
        self.btn_pivotXmin = btn_pivotXmin.component
        self.btn_pivotXmin.setGeometry(QRect(0, 80, 36, 36))
        self.btn_pivotXmin.setAutoFillBackground(False)

        btn_pivotXmax = UIButtonIcon("pivotXmax")
        btn_pivotXmax.set_icon(QIcon(iconpath_root + "pivot_maxX.png"))
        btn_pivotXmax.set_icon_size(iconsize)
        btn_pivotXmax.set_flat(True)
        btn_pivotXmax.bind_function_on_clicked(lambda: self.relocate_pivot(PivotRelocator.RelocateType.Max_X))
        btn_pivotXmax.construct(self.wdt_pivot)
        self.btn_pivotXmax = btn_pivotXmax.component
        self.btn_pivotXmax.setGeometry(QRect(160, 80, 36, 36))
        self.btn_pivotXmax.setAutoFillBackground(False)

        # center
        btn_pivotCenter = UIButtonIcon("pivotCenter")
        btn_pivotCenter.set_icon(QIcon(iconpath_root + "pivot_zero.png"))
        btn_pivotCenter.set_icon_size(40)
        btn_pivotCenter.set_flat(True)
        btn_pivotCenter.bind_function_on_clicked(lambda: self.relocate_pivot(PivotRelocator.RelocateType.Center))
        btn_pivotCenter.construct(self.wdt_pivot)
        self.btn_pivotCenter = btn_pivotCenter.component
        self.btn_pivotCenter.setGeometry(QRect(70, 70, 54, 54))
        self.btn_pivotCenter.setAutoFillBackground(False)

        self.horizontalLayout_3.addWidget(self.wdt_pivot)

        # spacer
        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        # end of content
        self.verticalLayout_7.addWidget(self.gbox_pivotContent)

        # pivot bake button
        btn_bakePivot = UIButton_JPEN("bake_pivot")
        btn_bakePivot.set_label_text_en("Bake")
        btn_bakePivot.set_label_text_jp("ベイクする")
        btn_bakePivot.bind_function_on_clicked(lambda: self.bake_pivot())
        btn_bakePivot.construct()
        self.btn_pivotBake = btn_bakePivot.component
        self.verticalLayout_7.addWidget(self.btn_pivotBake)

        # spacer
        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        icon7 = QIcon()
        icon7.addFile(u":/root/img/pivot_relocator/icon_pivot_relocator.png", QSize(), QIcon.Normal, QIcon.Off)
        parentUI.addTab(self.tab_pivot, icon7, "")

        self.btn_pivotZmin.setDefault(False)
        self.btn_pivotZmax.setDefault(False)
        self.btn_pivotYmax.setDefault(False)
        self.btn_pivotXmin.setDefault(False)
        self.btn_pivotYmin.setDefault(False)
        self.btn_pivotXmax.setDefault(False)
        self.btn_pivotCenter.setDefault(False)

        self.lbl_pivotIcon.setText("")
        self.lbl_pivotLabel.setText(QCoreApplication.translate("MainWindow", u"Pivot Relocator", None))
        self.lbl_pivotBase.setText("")
        self.btn_pivotZmin.setText("")
        self.btn_pivotZmax.setText("")
        self.btn_pivotYmax.setText("")
        self.btn_pivotXmin.setText("")
        self.btn_pivotYmin.setText("")
        self.btn_pivotXmax.setText("")
        self.btn_pivotCenter.setText("")
        parentUI.setTabText(parentUI.indexOf(self.tab_pivot), QCoreApplication.translate("MainWindow", u"Pivot", None))

        return self.tab_pivot

    def bake_pivot(self):
        selection = cmds.ls(sl=True)
        if len(selection) == 0:
            self.log_warning("オブジェクトが選択されていません","No object selected.")
            return
        
        cmds.select(selection[0])
        cmds.setToolTo("moveSuperContext")
        cmds.BakeCustomPivot()
        self.log_info("ピボットをベイクしました","Baked current pivot.")

    def relocate_pivot(self,relocateType : RelocateType):
        # コンポーネント選択だったらオブジェクト選択にする
        if cmds.selectMode(q=1, component=1) == 1:
            cmds.selectMode(object=1)

        selection = cmds.ls(sl=True)
        if len(selection) == 0:
            self.log_warning("オブジェクトが選択されていません","No object selected.")
            return
        
        for selected in selection:
            cmds.xform(selected,cp=True)
            bb_box = cmds.xform(selected,q=True,bb=True,ws=True)
            x_min,y_min,z_min,x_max,y_max,z_max = bb_box
            
        # get object center
        objectCenter = cmds.objectCenter(selection)

        match relocateType:
            case PivotRelocator.RelocateType.Min_X:
                cmds.move(x_min,[f"{selected}.scalePivot",f"{selected}.rotatePivot"],x=True,a=True)
            case PivotRelocator.RelocateType.Min_Y:
                cmds.move(y_min,[f"{selected}.scalePivot",f"{selected}.rotatePivot"],y=True,a=True)
            case PivotRelocator.RelocateType.Min_Z:
                cmds.move(z_min,[f"{selected}.scalePivot",f"{selected}.rotatePivot"],z=True,a=True)
            case PivotRelocator.RelocateType.Max_X:
                cmds.move(x_max,[f"{selected}.scalePivot",f"{selected}.rotatePivot"],x=True,a=True)
            case PivotRelocator.RelocateType.Max_Y:
                cmds.move(y_max,[f"{selected}.scalePivot",f"{selected}.rotatePivot"],y=True,a=True)
            case PivotRelocator.RelocateType.Max_Z:
                cmds.move(z_max,[f"{selected}.scalePivot",f"{selected}.rotatePivot"],z=True,a=True)
            case PivotRelocator.RelocateType.Center:
                cmds.xform(selected,cp=True)

        self.log_info("ピボットを移動しました: " + relocateType.name ,"Relocated pivot to: " + relocateType.name)
