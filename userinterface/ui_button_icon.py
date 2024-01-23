# ui_button_v2r_JPEN.py
# button component with vertical 2 row label JP / EN
from .ui_button_base import UIButtonBase

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class UIButtonIcon(UIButtonBase):
    def initialize(self):
        super().initialize()
        self.label_text = ""
        self.icon = None
        self.icon_size = QSize(16,16)
        self.flat = True

    # --- functions related to button ---
    # set icon
    def set_icon(self, icon):
        if self.is_constructed():
            self.component.setIcon(icon)
        self.icon = icon

    # set icon size
    def set_icon_size(self, size, size2 = None):
        if size2 is not None:
            iconsize = QSize(size,size2)
        else:
            iconsize = QSize(size,size)
            
        if self.is_constructed():
            self.component.setIconSize(iconsize)
        self.icon_size = iconsize

    # set flat
    def set_flat(self, flat):
        if self.is_constructed():
            self.component.setFlat(flat)
        self.flat = flat
        
    # --- functions related to ui ---
    # construct ui
    def construct_content(self,widget = None):
        super().construct_content(widget)
        self.component.setIcon(self.icon)
        self.component.setIconSize(self.icon_size)
        self.component.setFlat(self.flat)
        
    # construct

