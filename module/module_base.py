# module.py

from abc import ABCMeta, abstractmethod

class ModuleBase(metaclass=ABCMeta):
    def __init__(self,identifier = "Module Name"):
        self.identifier = identifier
        self.label = identifier
        self.ui = None
        self.icon = None
        self.font = None
        self.pixmap = None
        self.constructed = False
        self.initialize()

    def make_ui(self, parentUI = None):
        self.ui = self.construct_ui(parentUI)
        self.constructed = True
        return self.ui

    def set_identifier(self, identifier):
        self.identifier = identifier

    def set_label(self, label):
        self.label = label

    def set_icon(self, icon):
        self.icon = icon

    def set_font(self, font):
        self.font = font

    def set_pixmap(self, pixmap):
        self.pixmap = pixmap

    def get_identifier(self):
        return self.identifier
    
    def get_ui(self):
        return self.ui
    
    def is_constructed(self):
        return self.constructed
    
    def log(self, jp,en = ""):
        print("[" + self.identifier + "] " + jp + " / " + en)
    
    @abstractmethod
    def initialize(self):
        raise NotImplementedError()
    
    @abstractmethod
    def construct_ui(self, parentUI = None):
        raise NotImplementedError()