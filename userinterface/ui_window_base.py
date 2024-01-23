# ui_window_base.py:

from .ui_base import UIBase

import shiboken2 as shiboken

# OpenMayaUIをインポート
import maya.OpenMayaUI as OpenMayaUI

class UIWindowBase(UIBase):
    component_prefix = "window_"
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    parent = shiboken.wrapInstance(int(ptr), QWidget)

    def __init__(self,identifier,parent=None,name=None):
        super().__init__(identifier)
        self.component = QMainWindow()

    def construct_content(self,widget):
        pass
