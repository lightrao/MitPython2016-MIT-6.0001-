class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals=[]

    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if e not in self.vals:
            self.vals.append(e)
        
    def member(self, e):
        """ Assumes e is an integer
        Returns True if e is in self, and False otherwise """
        return e in self.vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self """
        if e in self.vals:
            self.vals.remove(e)
        
    def __str__(self):
        """ Returns a string representation of self """
        return '{'+','.join([str(e) for e in self.vals])+'}'
    
mySet=intSet()
mySet.insert(1)
mySet.insert(2)
print(mySet)
print(mySet.member('a'))
mySet.remove('b')
print(mySet)