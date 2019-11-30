from animal import Animal

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.set_name(name)
        self.friends=[]
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello.")
    def age_diff(self,other):
        diff=self.years-other.years
        print(abs(diff),"years difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.years)

if __name__=="__main__":
    p=Person("light",38)
    print(p)
    p.add_friend('neo')
    p.add_friend('nick')
    print(p.get_friends())
    p.speak()
    q=Person("Kasey",22)
    p.age_diff(q)
    q.age_diff(p)
    print(p.get_age())
    print(p.get_name())

