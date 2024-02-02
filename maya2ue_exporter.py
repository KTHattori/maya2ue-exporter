# Maya2UE Exporter

# import maya API
import maya.cmds as cmds;

# import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# import main window
from .userinterface.ui_mainwindow import GUI as MainWindow

def main():
    global main_window

    # Try to close window if it already exists
    try:main_window.close()
    except:pass

    # Create window
    app = QApplication.instance()
    main_window = MainWindow()
    main_window.show()
    
    app.exec_()