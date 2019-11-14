def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(5))


def fib_efficent(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib_efficent(n-1,d)+fib_efficent(n-2,d)
        d[n]=ans
        return ans
d={1:1,2:1}
print(fib_efficent(100,d))