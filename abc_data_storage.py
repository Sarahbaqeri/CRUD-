from abc import ABC,abstractmethod

class DataStorage(ABC):
    @abstractmethod
    def add(self,dict) -> None:
        pass 
    @abstractmethod
    def update(self,dict) ->None:
        pass
    @abstractmethod
    def read(self,id:int) ->dict:
        pass
    @abstractmethod
    def delete(self,id:int) -> None:
        pass
    #@abstractmethod
    #def list_all(self) ->list:
        #pass 