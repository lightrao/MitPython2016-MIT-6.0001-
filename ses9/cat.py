import animal

class Cat(animal.Animal):
    def speak(self):
        print("meow.")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.years)

if __name__=="__main__":
    myCat=Cat(3)
    myCat.set_name("Nick")
    print(myCat)
    myCat.speak()
    
    myAnimal=animal.Animal(99)
    print(myAnimal)
    # myAnimal.speak()
