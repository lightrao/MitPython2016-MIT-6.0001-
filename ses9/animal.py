class Animal(object):
    def __init__(self, age):
        self.years = age
        self.name = None

    def get_age(self):
        return self.years

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.years = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.years)


if __name__ == "__main__":
    a=Animal(4)
    a.set_name()
    print(a.get_name())
    a.set_name("lite")
    print(a.get_name())

    
    # myanimal = Animal(3)
    # myanimal.set_age(22)
    # myanimal.set_name("Peter")
    # myanimal.size="big"
    # print(myanimal.get_age())
    # print(myanimal.get_name())
    # print(myanimal.size)
    
