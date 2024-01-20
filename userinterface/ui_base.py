# ui_base.py:

from abc import ABCMeta, abstractmethod

class UIBase(metaclass=ABCMeta):
    def __init__(self,identifier):
        self.set_identifier(identifier)
        self.component = None
        self.constructed = False
        self.initialize()
  
    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_identifier(self):
        return self.identifier
    
    def is_constructed(self):
        return self.constructed
    
    def construct(self, widget = None):
        if self.is_constructed():
            return self.component
        self.construct_content(widget)
        self.constructed = True
        return self.component
    
    @abstractmethod
    def initialize(self):
        raise NotImplementedError()
    
    @abstractmethod
    def construct_content(self, widget = None):
        raise NotImplementedError()

