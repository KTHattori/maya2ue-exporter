# pivot relocator module for maya2ue exporter

import maya.cmds as cmds
from enum import Enum

# class definition of pivot relocator
class PivotRelocator:
    class RelocateType(Enum):
        Min_X = 0
        Min_Y = 1
        Min_Z = 2
        Max_X = 3
        Max_Y = 4
        Max_Z = 5
        Center = 6

    # member variables
    boundingBox = None # bounding box of selected object
    objectCenter = None # center of selected object
    applyAllFlag = False # apply boundary box to all selected if flag is true

    def __init__(self):
        pass

    def set_apply_all_flag(self, flag : bool):
        applyAllFlag = flag

    

# enum for pivot location


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
