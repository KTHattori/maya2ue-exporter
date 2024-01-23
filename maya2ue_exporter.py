# Maya2UE Exporter

# import maya API
import maya.cmds as cmds;

# import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# reloadを使用するためのモジュールをインポート
import importlib
import maya2ue.userinterface.ui_mainwindow as MainWindow ;importlib.reload(MainWindow)

def open():
    global mainWindow

    # Try to close window if it already exists
    try:mainWindow.close()
    except:pass

    # Create window
    app = QApplication.instance()
    mainWindow = MainWindow.GUI()
    mainWindow.show()
    
    app.exec_()

open()