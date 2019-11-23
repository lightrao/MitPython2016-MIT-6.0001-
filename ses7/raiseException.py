def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = not a number
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("In the else.")
        finally:
            print("In the finally.")
    print("At the bottom of function.")
    return ratios

l1=[1]
l2=["a"]
res=get_ratios(l1,l2)
print(res)