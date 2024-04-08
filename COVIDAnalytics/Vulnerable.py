from Human import Human


class Vulnerable(Human):
    def __init__(self, age, sickness):
        Human.__init__(self, age)
        self.sickness = sickness
