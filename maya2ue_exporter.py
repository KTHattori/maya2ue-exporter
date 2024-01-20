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

def excute():

    # get selection
    selection = cmds.ls(sl=True)
    if len(selection) == 0:
        cmds.warning("Please select mesh")
        return
    
    # get bounding box
    boundingBox = cmds.exactWorldBoundingBox(selection)

    # get object center
    objectCenter = cmds.objectCenter(selection)

    # print for debug
    print("min XYZ: " + str(boundingBox[0]) + ", " + str(boundingBox[1]) + ", " + str(boundingBox[2]))
    print("max XYZ: " + str(boundingBox[3]) + ", " + str(boundingBox[4]) + ", " + str(boundingBox[5]))
    print("center XYZ: " + str(objectCenter[0]) + ", " + str(objectCenter[1]) + ", " + str(objectCenter[2]))

    # set pivot to bottom of object
    cmds.move(0, boundingBox[1], 0, selection, absolute=True, worldSpace=True)


    # open file dialog
    # cmds.fileDialog2(fileFilter="FBX export(*.fbx)", dialogStyle=2, fileMode=0)


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