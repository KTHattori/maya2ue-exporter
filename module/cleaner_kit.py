import maya.cmds as cmds

def delete_history():
    cmds.DeleteAllHistory()

def freeze_transform():
    cmds.makeIdentity(apply=True, translate=True, rotate=True, scale=True)

def reset_transform():
    cmds.makeIdentity(apply=False, translate=True, rotate=True, scale=True)

def print_debug():
    print("debug")
