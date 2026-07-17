
#Implemention hide
#Hiding implementation (how its doing) data to user and shows necessary functionality only

from abc import ABC, abstractmethod

class BMW(ABC):

    @abstractmethod
    def engine(self):
        pass                # "How to do" is hided here (creating rule here, implementation in child classes)

class Audi(BMW):
    def engine(self):
        print("My engine is good")


obj = Audi()
obj.engine()

#One line definition - "what to do" only showing , "How to do" is hided. thats abstraction