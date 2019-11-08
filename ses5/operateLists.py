L=[0,1,2,3,4,5,6,7]

# del(L[2])
# print(L)

# a=L.pop()
# print(a,L)

# http://www.pythontutor.com/live.html#code=L%3D%5B2,1,3,6,3,7,0%5D%0AL.remove%282%29%0AL.remove%283%29%0Adel%28L%5B1%5D%29%0AL.pop%28%29&cumulative=false&curInstr=5&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
L=[2,1,3,6,3,7,0]
L.remove(2)
L.remove(3)
del(L[1])
L.pop()

