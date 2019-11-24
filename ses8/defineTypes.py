class Coordinate(object):
    # define attributes here
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'
    def __add__(self,other):
        x_sum=self.x+other.x
        y_sum=self.y+other.y
        return Coordinate(x_sum,y_sum)
    def __sub__(self,other):
        x_diff=self.x-other.x
        y_diff=self.y-other.y
        return Coordinate(x_diff,y_diff)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __lt__(self,other):
        origin=Coordinate(0,0)
        return self.distance(origin)<other.distance(origin)
    def __len__(self):
        return self.x+self.y


c=Coordinate(3,4)
d=Coordinate(6,7)
e=Coordinate(3,4)
f=Coordinate(0,0)

print(len(c))
print(len(d))

# print(c<d)
# print(c>d)

# print(c==d)
# print(c==c)
# print(c==e)

# print(c+d)
# print(d+c)
# print(c-d)
# print(d-c)

# print(c)
# print(type(c))
# print(Coordinate)
# print(type(Coordinate))

# print(type(10))
# print(type(int))

# print(isinstance(c,Coordinate))
# print(isinstance(22,Coordinate))

# print(c.distance(origin))
# print(origin.distance(c))
# print(Coordinate.distance(c,origin))
# print(Coordinate.distance(origin,c))