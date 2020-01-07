from animal import Animal

class Dog(Animal):
    def speak(self):
        print("ruff ruff.")
    def __str__(self):
        return "dog:"+str(self.name)+":"+str(self.years)

if __name__=="__main__":
    d = Dog(7)
    d.set_name("Ruffles")
    d.speak()
    print(d)
    print(Animal.__str__(d))