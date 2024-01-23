import maya.cmds as cmds
from enum import IntEnum
from .module_base import ModuleBase
from ..userinterface.ui_button_JPEN import UIButton_JPEN

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class UnrealExporter(ModuleBase):
    class ExportType(IntEnum):
        StaticMesh = 0
        Skeleton = 1
        SkeletalMesh = 2
    
    def __init__(self):
        super().__init__("Unreal Exporter")

    def initialize(self):
        self.exportType = UnrealExporter.ExportType.StaticMesh
        self.prefixComponent = None
        self.nameComponent = None

    def set_export_type(self, exportType : int):
        self.exportType = UnrealExporter.ExportType(exportType)
        if self.is_constructed() == False:
            return
        
        match self.exportType:
            case UnrealExporter.ExportType.StaticMesh:
                self.prefixComponent.setText("SM_")
            case UnrealExporter.ExportType.Skeleton:
                self.prefixComponent.setText("Skeleton_")
            case UnrealExporter.ExportType.SkeletalMesh:
                self.prefixComponent.setText("SK_")

    def excute_export(self):
        selected = cmds.ls(sl=True)
        if len(selected) == 0:
            self.log("オブジェクトが選択されていません","No object selected.")
            return

        match self.exportType:
            case UnrealExporter.ExportType.StaticMesh:
                # 選択オブジェクトのメッシュのみを選択
                meshes = cmds.ls(selection=True,dag=True,type="mesh")
                # ファイルを保存
                cmds.file(meshes,rename=self.prefixComponent.text() + self.nameComponent.text())
                cmds.file(meshes,save=True, type="fbx")
                # ログを出力
                self.log("メッシュのみをエクスポートしました。","Exported meshes.")
            case UnrealExporter.ExportType.Skeleton:
                # 選択オブジェクトのメッシュのみを選択
                joints = cmds.ls(selection=True,dag=True,type="joint")
                # ファイルを保存
                cmds.file(joints,rename=self.prefixComponent.text() + self.nameComponent.text())
                cmds.file(joints,save=True, type="fbx")
                # ログを出力
                self.log("ジョイントのみをエクスポートしました。","Exported joints.")
            case UnrealExporter.ExportType.SkeletalMesh:
                # 選択オブジェクトのメッシュのみを選択
                meshes = cmds.ls(selection=True,dag=True,type="mesh")
                # ファイルを保存
                cmds.file(meshes,rename=self.prefixComponent.text() + self.nameComponent.text())
                cmds.file(meshes,save=True, type="fbx")
                # ログを出力
                self.log("メッシュとジョイントをエクスポートしました。","Exported meshes and joints.")


    def construct_ui(self, parentUI = None):  
        font = QFont()
        font.setPointSize(9)
        self.frm_export = QFrame(parentUI)
        self.frm_export.setObjectName(u"frm_export")

        self.frm_export.setFont(font)
        self.frm_export.setFrameShape(QFrame.StyledPanel)
        self.frm_export.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6 = QVBoxLayout(self.frm_export)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.wdt_export = QGroupBox(self.frm_export)
        self.wdt_export.setObjectName(u"wdt_export")
        self.wdt_export.setFont(font)
        self.wdt_export.setAlignment(Qt.AlignCenter)
        self.wdt_export.setFlat(True)
        self.wdt_export.setCheckable(False)
        self.verticalLayout_8 = QVBoxLayout(self.wdt_export)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        # Export Type Selector
        self.cbx_exporttype = QComboBox(self.wdt_export)
        self.cbx_exporttype.addItem("メッシュのみ - Meshes Only (Static Mesh)")
        self.cbx_exporttype.addItem("ジョイントのみ - Joints Only (Skeleton)")
        self.cbx_exporttype.addItem("メッシュ + ジョイント - Meshes + Joints (Skeletal Mesh)")
        self.cbx_exporttype.setObjectName(u"cbx_exporttype")
        self.cbx_exporttype.currentIndexChanged.connect(self.set_export_type)

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

        self.prefixComponent = self.led_pref_input
        self.nameComponent = self.led_body_input

        self.horizontalLayout.addWidget(self.wdt_body_input)

        # Export Button
        btn_export = UIButton_JPEN("btn_export")
        btn_export.set_label_text_en("Export")
        btn_export.set_label_text_jp("エクスポート")
        btn_export.bind_function_on_clicked(lambda: self.excute_export())
        self.btn_export = btn_export.component
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.btn_export)
        self.verticalLayout_8.addWidget(self.wdt_rename)
        self.verticalLayout_6.addWidget(self.wdt_export)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.wdt_export.setTitle(QCoreApplication.translate("MainWindow", u" Export ", None))
        self.lbl_pref_input.setText(QCoreApplication.translate("MainWindow", u"Prefix", None))
        self.lbl_body_input.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Export\n"
"\u30a8\u30af\u30b9\u30dd\u30fc\u30c8", None))
        return self.frm_export
