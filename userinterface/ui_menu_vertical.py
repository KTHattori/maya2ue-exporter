# ui_menu_vertical.py
# button component with vertical 2 row label JP / EN
from . import ui_base
from . import ui_button_base

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Element():
    def __init__(self):
        self.button = None
        self.spacer_bottom = None
        self.spacer_top = None

class UIMenuVertical(ui_base.UIBase):
    def initialize(self):
        self.elements = []
        
    # --- functions related to ui ---
    def add_element(self,button):
        if self.is_constructed():
            # make element container
            element = Element()

            # add topside spacer
            element.spacer_top = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.baseLayout.addItem(element.spacer_top)

            # add button
            element.button = button.construct(self.component)
            self.baseLayout.addWidget(element.button)
                        
            # add bottomside spacer
            element.spacer_bottom = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.baseLayout.addItem(element.spacer_bottom)

        self.elements.append(element)

    def create_element(self,label,function):
        button = ui_button_base.UIButtonBase(ui_button_base.UIButtonBase.component_prefix + self.identifier + "_" + label)
        button.set_label_text(label)
        button.bind_function_on_clicked(function)
        self.add_element(button)

    def remove_element(self,element):
        if self.is_constructed():
            self.baseLayout.removeWidget(element.spacer_top)
            self.baseLayout.removeWidget(element.button)
            self.baseLayout.removeWidget(element.spacer_bottom)

        self.elements.remove(element)

    # construct ui
    def construct_content(self,widget):
        self.component = QWidget(widget)

        # base vertical layout
        self.baseLayout = QVBoxLayout(self.component)
        self.baseLayout.setObjectName("vlo_" + self.identifier)

        # for each buttons
        for button in self.elements:
            # add button
            self.add_element(button)

        QMetaObject.connectSlotsByName(self.component)

    # construct

