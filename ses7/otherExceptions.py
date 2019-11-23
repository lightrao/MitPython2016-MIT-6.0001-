try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    # raise Exception("descriptive string")
except:
    print("Something went very wrong.")
else:
    print("In the else.")
finally:
    print("In the finally.")

print("At the bottom.")