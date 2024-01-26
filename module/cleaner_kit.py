from .module_base import ModuleBase
from ..userinterface.ui_menu_vertical import UIMenuVertical
from ..userinterface.ui_button_JPEN import UIButton_JPEN
import maya.cmds as cmds
import maya.mel as mel

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class CleanerKit(ModuleBase):
    def __init__(self):
        super().__init__("Cleaner Kit")

    def initialize(self):
        pass

    # functions
    def reset_transform(self):
        selected = cmds.ls(sl=True)
        if len(selected) == 0:
            self.log_warning("オブジェクトが選択されていません","No object selected.")
            return
    
        cmds.makeIdentity(selected[0],apply=False, t=1, r=1, s=1, n=0)
        self.log_success("トランスフォームをリセットしました。","Resetted transform.")

    def freeze_transform(self):
        selected = cmds.ls(sl=True)
        if len(selected) == 0:
            self.log_warning("オブジェクトが選択されていません","No object selected.")
            return
        
        cmds.makeIdentity(selected[0],apply=True, t=1, r=1, s=1, n=0)
        self.log_success("トランスフォームをフリーズしました。","Freezeed transform.")
    
    def delete_unused_nodes(self):
        mel.eval("MLdeleteUnused;")
        self.log_success("未使用ノードを削除しました。","Deleted unused nodes.")

    def delete_history(self):
        cmds.DeleteAllHistory()
        self.log_success("全ヒストリを削除しました。","Deleted all history.")

    def construct_ui(self, parentUI = None):
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)

        self.tab_clean = QWidget()
        self.tab_clean.setObjectName(u"tab_clean")
        self.verticalLayout_3 = QVBoxLayout(self.tab_clean)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.wdt_cleanerLabel = QWidget(self.tab_clean)
        self.wdt_cleanerLabel.setObjectName(u"wdt_cleanerLabel")
        self.wdt_cleanerLabel.setMaximumSize(QSize(16777215, 46))
        self.wdt_cleanerLabel.setFont(font)
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
        self.lbl_cleanerLabel.setFont(font)

        self.horizontalLayout_7.addWidget(self.lbl_cleanerLabel)
        self.verticalLayout_3.addWidget(self.wdt_cleanerLabel)

        # make cleaner menu
        self.gbx_cleanerContent = QGroupBox(self.tab_clean)
        self.gbx_cleanerContent.setObjectName(u"gbx_cleanerContent")
        self.gbx_cleanerContent.setAlignment(Qt.AlignCenter)
        self.gbx_cleanerContent.setFlat(True)
        self.gbx_cleanerContent.setCheckable(False)

        vlo_cleaner = QVBoxLayout(self.gbx_cleanerContent)
        vlo_cleaner.setObjectName(u"vlo_cleaner")
        self.verticalLayout_3.addWidget(self.gbx_cleanerContent)

        self.cleanerMenu = UIMenuVertical("cleaner")
        cleanerMenuWidget = self.cleanerMenu.construct(self.gbx_cleanerContent)

        btn_reset_transform = UIButton_JPEN("reset_transform")
        btn_reset_transform.set_label_text_en("Reset Transform")
        btn_reset_transform.set_label_text_jp("トランスフォームのリセット")
        btn_reset_transform.bind_function_on_clicked(lambda: self.reset_transform())

        btn_freeze_transform = UIButton_JPEN("freeze_transform")
        btn_freeze_transform.set_label_text_en("Freeze Transform")
        btn_freeze_transform.set_label_text_jp("トランスフォームのフリーズ")
        btn_freeze_transform.bind_function_on_clicked(lambda: self.freeze_transform())

        btn_delete_unused_nodes = UIButton_JPEN("delete_unused_nodes")
        btn_delete_unused_nodes.set_label_text_en("Delete Unused Nodes")
        btn_delete_unused_nodes.set_label_text_jp("未使用ノードの削除")
        btn_delete_unused_nodes.bind_function_on_clicked(lambda: self.delete_unused_nodes())

        btn_delete_history = UIButton_JPEN("delete_history")
        btn_delete_history.set_label_text_en("Delete All History")
        btn_delete_history.set_label_text_jp("全ヒストリの削除")
        btn_delete_history.bind_function_on_clicked(lambda: self.delete_history())

        self.cleanerMenu.add_element(btn_reset_transform)
        self.cleanerMenu.add_element(btn_freeze_transform)
        self.cleanerMenu.add_element(btn_delete_unused_nodes)
        self.cleanerMenu.add_element(btn_delete_history)

        vlo_cleaner.addWidget(cleanerMenuWidget)

        icon8 = QIcon()
        icon8.addFile(u":/root/img/cleaner_kit/icon_cleaner_kit.png", QSize(), QIcon.Normal, QIcon.Off)
        parentUI.addTab(self.tab_clean, icon8, "")

        self.lbl_cleanerIcon.setText("")
        self.lbl_cleanerLabel.setText(QCoreApplication.translate("MainWindow", u"Cleaner Kit", None))
        parentUI.setTabText(parentUI.indexOf(self.tab_clean), QCoreApplication.translate("MainWindow", u"Clean", None))

        return self.tab_clean