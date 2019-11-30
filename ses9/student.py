import random
from person import Person

class Student(Person):
    def __init__(self,name,age,major=None):
        Person.__init__(self,name,age)
        self.major=major
    def change_major(self,major):
        self.major=major
    def get_major(self):
        return self.major
    def speak(self):
        r=random.random()
        if r<0.25:
            print("I have homework.")
        elif 0.25<=r<0.5:
            print("I need sleep.")
        elif 0.5<=r<0.75:
            print("I should eat.")
        else:
            print("I am watching Tv.")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.years)+":"+str(self.major)

if __name__=="__main__":
    s=Student("Albert",55,"math")
    print(s)
    s.change_major("phsics")
    print(s)
    s.speak()
