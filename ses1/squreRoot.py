def squreRoot(x):
    g = 1
    delta = 0.00000001

    while True:
        if x - g*g < delta and x - g*g > -delta:
            break
        g = (g + x/g)/2
      
    return g

print(squreRoot(81))



