# ui_button_v2r_JPEN.py
# button component with vertical 2 row label JP / EN
from . import ui_button_base

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class UIButton_JPEN(ui_button_base.UIButtonBase):
    def initialize(self):
        super().initialize()
        self.label_text_en = "Button"
        self.label_text_jp = "ボタン名"

    # --- functions related to button ---
    # set button text (english)
    def set_label_text_en(self, text):
        if self.is_constructed():
            self.component.setText(self.label_text_jp + "\n" + text)
        self.label_text_en = text
        self.set_label_text(self.label_text_jp + "\n" + text)

    # set button text (japanese)
    def set_label_text_jp(self, text):
        if self.is_constructed():
            self.component.setText(text + "\n" + self.label_text_en)
        self.label_text_jp = text
        self.set_label_text(text + "\n" + self.label_text_en)
        
    # --- functions related to ui ---
    # construct ui
    def construct_content(self,widget = None):
        super().construct_content(widget)
        self.component.setText(self.label_text_jp + "\n" + self.label_text_en)
    # construct

