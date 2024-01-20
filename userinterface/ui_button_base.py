# ui_button_base.py:

from . import ui_base

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class UIButtonBase(ui_base.UIBase):
    component_prefix = "btn_"

    def initialize(self):
        self.label_text = "Button"
        self.bound_function = None
        self.enabled = True

    # --- appearance ---
    def set_label_text(self, text):
        if self.is_constructed():
            self.component.setText(text)

        self.label_text = text

    def get_label_text(self):
        return self.label_text
    
    # --- logic ---
    def set_button_enabled(self, enabled):
        if self.is_constructed():
            self.component.setEnabled(enabled)
        self.enabled = enabled
        
    def bind_function_on_clicked(self, function):
        if self.is_constructed():
            self.component.clicked.connect(function)
        self.bound_function = function
        print("bound function: " + str(self.bound_function))

    def get_bound_function(self):
        return self.bound_function

    def construct_content(self,widget = None):
        # construct button
        self.component = QPushButton(widget)
        self.component.setObjectName(self.component_prefix + self.identifier)
        self.component.setLayoutDirection(Qt.LeftToRight)

        # set label text
        self.component.setText(self.label_text)

        # bind function
        if self.bound_function is not None:
            self.component.clicked.connect(self.bound_function)

        # set enabled
        self.component.setEnabled(self.enabled)