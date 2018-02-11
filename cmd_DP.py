from abc import ABC, abstractmethod
import random

class Chef:
    def __init__(self,foo,bar):
        self.foo = foo
        self.bar = bar
        self._obs =[]
        self.result = None
        
    def make_apple(self):
        print("Chef is preparing " + self.foo)
        self.__result(self.foo)
        self.notify()
    
    def make_orange(self):
        print("prepare " + self.bar)
        self.__result(self.foo)
        self.notify()
    
    def attach(self, waiter):
        self._obs.append(waiter)
    
    def notify(self):
        for ob in self._obs:
            ob.update(self.result)
    
    def __result(self, food):
        if random.choice([0,1]):
            self.result = "%s is ready" % (food,)
        else:
            self.result = "No %s, sorry##############" % (food,)
        

class Order(ABC):
    def __init__(self,temp=None):
        self.receiver=temp
    @abstractmethod
    def exec_order(self):
        """pass"""

class AppleOrder(Order):
    def exec_order(self):
        self.receiver.make_apple()

class OrangeOrder(Order):
    def exec_order(self):
        self.receiver.make_orange()

class Waiter:
    def __init__(self):
        self.orders =[]
        self.results =[]
        
    def add_orders(self,*order):
        self.orders.extend([*order])

    def set_orders(self,new_orders):
        self.orders = new_orders

    def notify(self):
        for order in self.orders:
            #print("Waiter is adding order")
            order.exec_order()

    def update(self, food):
        if "#" in food:
            print(food + "bad luck\n")
            self.results.append(False)
        else:
            print("good luck, dish is ready\n")
            self.results.append(True)

if __name__ == "__main__":
    chef=Chef("apple","orange")
    cmd=AppleOrder(chef)
    cmd2=OrangeOrder(chef)
    girl=Waiter()
    chef.attach(girl)
    for _ in range(2):
        girl.add_orders(cmd,cmd2,cmd,cmd2,)
    girl.notify()
    print("retry!")
    print(girl.results)
    new_orders = [girl.orders[i] for i,j in enumerate(girl.results) if not j]
    print(len(new_orders))
    girl.set_orders(new_orders)
    girl.notify()
