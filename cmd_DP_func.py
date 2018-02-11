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
    def chooseChef(self,chef):
        self.chef = chef
    def SetCmd(self,command):
        self.order.append(command)
        print("Add Order")
    def Notify(self):
        for cmd in self.order:
            cmd(self.chef)
            

if __name__ == "__main__":
    chef2=Chef2()
    girl=Waiter(chef2)
    girl.SetCmd(applePieCmd)
    girl.SetCmd(chickenCmd)
    girl.Notify()
    chef=Chef()
    girl.chooseChef(chef)
    girl.Notify()
