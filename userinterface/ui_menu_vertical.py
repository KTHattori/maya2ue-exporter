# ui_menu_vertical.py
# button component with vertical 2 row label JP / EN
from . import ui_base
from . import ui_button_base

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class UIMenuVertical(ui_base.UIBase):
    def initialize(self):
        self.buttons = []
        
    # --- functions related to ui ---
    def add_button(self,button):
        if self.is_constructed():
            self.verticalLayout.addWidget(button.construct(self.component))

        self.buttons.append(button)

    def create_button(self,label,function):
        button = ui_button_base.UIButtonBase(self.identifier + "_" + label)
        button.set_label_text(label)
        button.bind_function_on_clicked(function)
        self.add_button(button)

    def remove_button(self,button):
        if self.is_constructed():
            self.verticalLayout.removeWidget(button.construct(self.component))

        self.buttons.remove(button)

    # construct ui
    def construct_content(self,widget):
        self.component = QWidget(widget)

        # vertical layout
        self.verticalLayout = QVBoxLayout(self.component)
        self.verticalLayout.setObjectName("vlo_" + self.identifier)

        # for each buttons
        for button in self.buttons:
            # add topside spacer
            spacer_top = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.verticalLayout.addItem(spacer_top)

            # add button
            self.add_button(button)
            
            # add bottomside spacer
            spacer_bottom = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.verticalLayout.addItem(spacer_bottom)

        QMetaObject.connectSlotsByName(self.component)

    # construct

