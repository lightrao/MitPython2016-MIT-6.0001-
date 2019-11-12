def fact(n):
    product=1
    while n>0:
        product*=n
        n-=1
    return product

def factorial_iter(n):
    prod=1
    for i in range(1,n+1):
        prod*=i
    return prod

print(fact(4))
print(factorial_iter(4))

