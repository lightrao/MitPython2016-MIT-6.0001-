def g(x):
    def h():
        x='abc'
        print('h:x =',x)
    x=x+1
    print('g:x =',x)
    h()
    return x

x=3
z=g(x)
print(x)
print(z)

