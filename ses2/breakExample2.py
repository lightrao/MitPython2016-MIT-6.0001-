a = 0
while a <= 5:
    b = 0
    while b <= 5:
        print(a, b)
        b += 1
        if b == 3:
            break
        print("buttom of inner while.")
    a += 1
    print("buttom of outter while.")
