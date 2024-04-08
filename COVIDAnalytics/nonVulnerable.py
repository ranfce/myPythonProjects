from Human import Human


class NonVulnerable(Human):
    def __init__(self, age, address):
        Human.__init__(self, age)
        self.address = address
