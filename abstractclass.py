#import necessary modules
from abc import ABC, abstractmethod

#create base class
class Absclass(ABC):
    #function to print a value
    def print(self, x):
        print("Passed value: ", x)
    #abstract method
    @abstractmethod
    def task(self):
        print("We are in the Absclass")
        
#create sub class
class test_class(Absclass):
    def task(self):
        print("We are inside the test_class task")
        
#object of test class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

    