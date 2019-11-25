class Fraction(object):
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)
    def __float__(self):
        return self.numerator/self.denominator
    def __add__(self,other):
        top=self.numerator*other.denominator+self.denominator*other.numerator
        bottom=self.denominator*other.denominator
        return Fraction(top,bottom)
    def __sub__(self,other):
        top=self.numerator*other.denominator-self.denominator*other.numerator
        bottom=self.denominator*other.denominator
        return Fraction(top,bottom)
    def invert(self):
        return Fraction(self.denominator,self.numerator)
    

f=Fraction(1,2)
g=Fraction(3,4)
print(f.invert())