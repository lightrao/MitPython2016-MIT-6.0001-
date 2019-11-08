# swap variable values
x=1
y=2

# x=y
# y=x
# print(x,y)

# temp=x
# x=y
# y=temp
# print(x,y)

# x,y=y,x
# print(x,y)

# return more than one value from a function
def quotient_and_remainder(x,y):
    '''
    返回商和余数
    '''
    q=x//y
    r=x%y
    return(q,r)

(quot,rem)=quotient_and_remainder(11,3)
print(quot,rem)
