class Human:
    def __init__(self, age):
        self.age = age
        self.isSick = False
        self.sickDay = -1

    def printInfo(self):
        print("Age =", self.age, end="")
        if self.isSick:
            print(" Sick person with sickness day = ", self.sickDay, end="")
        else:
            print(" Not a sick person", end="")
        print()
