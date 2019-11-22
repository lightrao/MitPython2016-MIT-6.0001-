def sqrt(x,eps=0.00000001):
    """ Assumes x, eps floats, x >= 0, eps > 0
    Returns res such that x-eps <= res*res <= x+eps """
    res = 1    
    while True:
        if x-eps < res*res < x+eps:
            break
        res = (res + x/res)/2
    return res

# Test function
if __name__ == "__main__": 
    print(sqrt(2,0.0001)**2)


