def cubeRoot(cube = 0, epsilon = 0.01):
    num_guesses = 0
    if abs(cube) >= 1:
        low = -abs(cube)
        high = abs(cube)
    else:
        low = -1
        high = 1
    guess = (high + low)/2
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        num_guesses += 1
    return(num_guesses, guess, cube)

num_guesses, guess, cube = cubeRoot(cube=-5122454616148,epsilon=0.001)
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)