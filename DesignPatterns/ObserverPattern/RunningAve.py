# -*- coding: utf-8 -*-
"""
Oberver Design Pattern 
    Running Average 
"""

class Subject:
    
    def __init__(self):
        self._observers = []
    def notify(self,modifier = None):
        
        for observer in self._observers :
            if modifier != observer:
                observer.update(self)
                break
    
    def attach(self,observer):
        
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self,observer):
        
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
class Data(Subject):
    
    def __init__(self,number=''):
        Subject.__init__(self)
        self.number = number
        self._data = 0
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self,value):
        self._data = value
        self.notify()

class RunningAverage:
    _mean = 0
    def update(self,number):
        RunningAverage._mean +=number._data
        print("The average of given numbers so far is : ",RunningAverage._mean/len(number._observers))
    
if __name__ == "__main__" :
    number1 = Data('10')
    
    while(1):
        answer = input("Type a number : ")
        if answer == '':
            break
        obj = RunningAverage()
        number1.attach(obj)
        number1.data = int(answer)
    
