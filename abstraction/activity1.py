from abc import ABC,abstractmethod
class third(ABC):
    def display(self,a):
        print('the value is',a)
    @abstractmethod
    def task(self):
        print('we are inside the third class task')
class first(third):
    def task(self):
        print('we are inside the first task')
obj=first()
obj.task()
obj.display(40)

