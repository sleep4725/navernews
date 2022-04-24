from abc import *

'''
    @author JunHyeon.Kim
'''
class Templete(metaclass=ABCMeta):
    
    @abstractmethod
    def getData(self):
        pass
    
    @abstractmethod
    def jsonFileGenerate(self):
        pass