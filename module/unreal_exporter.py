import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
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
        self.name_prefix = "SM_"
        self.name_body = self.get_scene_name().split(".")[0]
        print(self.name_body)

    def get_scene_name(self):
        return cmds.file(query=True,sceneName=True,shortName=True)
    
    def get_scene_path(self):
        return cmds.file(query=True,sceneName=True)

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

    def export_as_fbx(self,path):
        # FBXエクスポート設定
        cmds.FBXResetExport()  # リセット
        cmds.FBXExportHardEdges('-v', True) # ハードエッジをエクスポートする
        cmds.FBXExportSmoothingGroups('-v', True) # スムージンググループをエクスポートする
        cmds.FBXExportTangents('-v', True)  # 接線をエクスポートする
        cmds.FBXExportInputConnections("-v", 0) # 入力接続をエクスポートしない
        cmds.FBXExportCameras("-v", 0) # カメラをエクスポートしない
        cmds.FBXExportConstraints("-v", 0) # コンストレイントをエクスポートしない
        cmds.FBXExportLights("-v", 0) # ライトをエクスポートしない
        cmds.FBXProperty("Export|IncludeGrp|Geometry|Triangulate", "-v", 1) # 三角メッシュに変換する
        cmds.FBXProperty('Export|IncludeGrp|Animation', '-v', 0)    # アニメーションをエクスポートしない

        # エクスポート
        mel.eval('FBXExport -f "{}" -s;'.format(path))

        # ログ出力
        self.log_success("エクスポートが完了しました","Export completed.")

    def export_on_clicked(self):
        selected = cmds.ls(sl=True)
        if len(selected) == 0:
            self.log_warning("オブジェクトが選択されていません","No object selected.")
            return

        match self.exportType:
            case UnrealExporter.ExportType.StaticMesh:
                # 選択オブジェクトのメッシュのみを選択
                cmds.select(cmds.ls(selection=True,dag=True,type="mesh"))
                meshes = cmds.ls(selection=True)
                if len(meshes) == 0:
                    self.log_error("有効なメッシュが存在しません","No mesh selected.")
                    return

            case UnrealExporter.ExportType.Skeleton:
                # 選択オブジェクトのジョイントのみを選択
                cmds.select(cmds.ls(selection=True,dag=True,type="joint"))
                joints = cmds.ls(selection=True)
                if len(joints) == 0:
                    self.log_error("有効なジョイントが存在しません","No joint selected.")
                    return

            case UnrealExporter.ExportType.SkeletalMesh:
                pass
    

        # 元のファイル名の保存
        original_name = self.get_scene_name()

        # エクスポートするファイル名の取得
        export_name = self.prefixComponent.text() + self.nameComponent.text() + ".fbx"

        # 現在のファイルパスを取得
        current_path = self.get_scene_path()

        # ファイルパスを元にエクスポート先のパスを生成
        export_path = current_path.replace(original_name, export_name)

        # --- もし同名のファイルが存在したら確認 ---
        # TODO : 実装
        if cmds.file(export_path,query=True,exists=True):
            pass

        # --- エクスポート ---
        self.export_as_fbx(export_path)




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
        self.led_pref_input.setText(self.name_prefix)

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
        self.led_body_input.setText(self.name_body)

        self.verticalLayout_5.addWidget(self.led_body_input)

        self.prefixComponent = self.led_pref_input
        self.nameComponent = self.led_body_input

        self.horizontalLayout.addWidget(self.wdt_body_input)

        # Export Button
        btn_export = UIButton_JPEN("btn_export")
        btn_export.set_label_text_en("Export")
        btn_export.set_label_text_jp("エクスポート")
        btn_export.bind_function_on_clicked(lambda: self.export_on_clicked())
        self.btn_export = btn_export.construct()
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.btn_export)
        self.verticalLayout_8.addWidget(self.wdt_rename)

        # Export Path Label
        # self.lbl_exportpath = QLabel()
        # self.lbl_exportpath.setObjectName(u"lbl_exportpath")
        # self.lbl_exportpath.setAlignment(Qt.AlignCenter)
        # self.lbl_exportpath.setTextInteractionFlags(Qt.TextSelectableByMouse)
        # self.lbl_exportpath.setText(self.get_scene_path())
        # self.verticalLayout_8.addWidget(self.lbl_exportpath)

        self.verticalLayout_6.addWidget(self.wdt_export)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.wdt_export.setTitle(QCoreApplication.translate("MainWindow", u" Export ", None))
        self.lbl_pref_input.setText(QCoreApplication.translate("MainWindow", u"Prefix", None))
        self.lbl_body_input.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Export\n"
"\u30a8\u30af\u30b9\u30dd\u30fc\u30c8", None))
        return self.frm_export
