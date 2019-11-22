def abs(x):
    """ Assumes x is an int
    Returns x if x>=0 and –x otherwise """
    if x < -1:
        return -x
    else:
        return x

print(abs(2))
print(abs(-2))
print(abs(1))
print(abs(-1))
print(abs(0.5))
print(abs(-0.5))