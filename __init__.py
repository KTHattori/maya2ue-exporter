import importlib
from . import maya2ue_exporter as exporter; importlib.reload(exporter)

def open():
    importlib.reload(exporter)
    exporter.main()