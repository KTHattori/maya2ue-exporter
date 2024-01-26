# logger.py

from enum import IntEnum

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Logger():
    class Level(IntEnum):
        Debug = -1
        Info = 0
        Success = 1
        Warning = 2
        Error = 3


    instance = None
    label_component = None

    @classmethod
    def __new__(cls, parentUI = None):
        if cls.instance is None:
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    @classmethod
    def emit(cls,caller,message,level = Level.Info):
        cls.label_component.setText("[{0}] {1}".format(caller.get_identifier(),message))
        cls.apply_level_style(level)

    @classmethod
    def clear(cls):
        cls.label_component.setText("")

    @classmethod
    def apply_level_style(cls, level):
        match level:
            case Logger.Level.Debug:
                cls.set_font_style(9,False,True,False)
                cls.set_font_color(128,128,128)
            case Logger.Level.Info:
                cls.set_font_style(9,False,False,False)
                cls.set_font_color(255,255,255)
            case Logger.Level.Success:
                cls.set_font_style(9,True,False,False)
                cls.set_font_color(0,255,0)
            case Logger.Level.Warning:
                cls.set_font_style(9,True,False,True)
                cls.set_font_color(255,128,0)
            case Logger.Level.Error:
                cls.set_font_style(9,True,False,True)
                cls.set_font_color(255,0,0)

    @classmethod
    def set_font_color(cls,r,g,b):
        cls.label_component.setStyleSheet("color: rgb({0},{1},{2});".format(r,g,b))

    @classmethod
    def set_font_style(cls,size = -1,bold = False,italic = False,underline = False):
        font = QFont()

        # set font size
        if size == -1:
            font.setPointSize(9)
        else:
            font.setPointSize(size)

        # set font style
        font.setBold(bold)
        font.setItalic(italic)
        font.setUnderline(underline)

        # apply font
        cls.label_component.setFont(font)
        
    @classmethod
    def make_ui(cls, parentUI = None):
        font = QFont()
        font.setPointSize(9)
        frm_logger = QFrame(parentUI)
        frm_logger.setObjectName(u"frm_logger")

        frm_logger.setFont(font)
        frm_logger.setFrameShape(QFrame.StyledPanel)
        frm_logger.setFrameShadow(QFrame.Raised)

        verticalLayout = QVBoxLayout(frm_logger)
        verticalLayout.setObjectName(u"vlo_logger")
        
        gbx_logger = QGroupBox(frm_logger)
        gbx_logger.setObjectName(u"gbx_logger")
        gbx_logger.setFont(font)
        gbx_logger.setAlignment(Qt.AlignCenter)
        gbx_logger.setFlat(True)
        gbx_logger.setCheckable(False)
        gbx_logger.setTitle("Logger")
        verticalLayout2 = QVBoxLayout(gbx_logger)
        verticalLayout2.setObjectName(u"vlo_logger_2")

        lbl_content = QLabel(gbx_logger)
        lbl_content.setObjectName(u"lbl_logger_content")

        verticalLayout2.addWidget(lbl_content)
        verticalLayout.addWidget(gbx_logger)

        cls.label_component = lbl_content

        return frm_logger

    

# TODO: 以下の通り修正
# logger は module から独立させる
# module から log() を呼び出すようにする
# module は log() を呼び出すときに、自分のidentifierを渡す
# そうすることにより、呼び出した module の identifier が表示される