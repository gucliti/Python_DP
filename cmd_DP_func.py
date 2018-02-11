class Chef:
    def makeApplePie(self):
        print("Apple Pie")
    def makeChicken(self):
        print("Chicken")


class Chef2:
    def makeApplePie(self):
        print("Apple Pie 2")
    def makeChicken(self):
        print("Chicken 2")


def applePieCmd(actor):
    actor.makeApplePie()


def chickenCmd(actor):
    actor.makeChicken()


class Waiter:
    def __init__(self, chef):
        self.order =[]
        self.chef = chef
        self.order2 =[]
    
    #cmd already has a binding target
    def SetCmd(self,command):
        self.order.append(command)
        print("Add Order")
    def Notify(self):
        for cmd in self.order:
            cmd()
    
    #cmd is just pure func
    def chooseChef(self,chef):
        self.chef = chef
    def SetCmd2(self,command):
        self.order2.append(command)
        print("Add Order")
    def Notify2(self):
        for cmd in self.order2:
            cmd(self.chef)
            

if __name__ == "__main__":
    chef=Chef()
    waiter=Waiter(chef)
    
    #create cmd, binding target
    waiter.SetCmd(lambda:applePieCmd(chef))
    waiter.SetCmd(lambda:chickenCmd(chef))
    waiter.Notify()
    
    #the other way, func with args.
    chef2=Chef()
    waiter.chooseChef(chef2)
    waiter.SetCmd2(applePieCmd)
    waiter.SetCmd2(chickenCmd)
    waiter.Notify2()
