from animal import Animal


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __str__(self):
        # return "rabbit:"+"name is "+str(self.name)+":"+"age is "+str(self.years)+":"+"parent is {"+str(self.parent1)+","+str(self.parent2)+"}"+":number is "+self.get_rid()
        return "rabbit number is "+self.get_rid()

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self,other):
        parent_same=self.parent1.rid==other.parent1.rid and self.parent2.rid==other.parent2.rid
        parent_oppsite=self.parent1.rid=other.parent2.rid and self.parent2.rid==other.parent1.rid
        return parent_same or parent_oppsite


if __name__ == "__main__":
    r1 = Rabbit(5)
    r2 = Rabbit(3)
    r3=r1+r2
    r4=r2+r1
    r5=r1+r3
    print(r3==r4)
    print(r4==r3)
    print(r5==r3)

    # print(r3.get_parent1())
    # print(r3.get_parent2())
    # print(r3)
