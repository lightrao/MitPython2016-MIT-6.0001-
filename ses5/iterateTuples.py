def get_data(aTuple):
    """
    输入：嵌套元组
    输出：（最小值，最大值，单词个数）
    """
    nums=()
    words=()
    for t in aTuple:
        nums=nums+(t[0],)
        if t[1] not in words:
            words+=(t[1],)
    min_n=min(nums)
    max_n=max(nums)
    unique_words=len(words)
    print(type(nums),nums)
    print(type(words),words)
    return(min_n,max_n,unique_words)

aTuple=((2,'apple'),(5,'orange'),(18,'banana'),(33,'pear'),(4,'apple'),(17,'orange'))
# print(type(aTuple),aTuple)
zd,zx,gs=get_data(aTuple)
print(zd,zx,gs)


