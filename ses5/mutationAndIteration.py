def remove_dups(L1,L2):
    """
    从L1中移除L2中包含的元素
    """
    L1_copy=L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1=[1,2,3,4]
L2=[1,2,5,6]
remove_dups(L1,L2)
print(L1,L2)