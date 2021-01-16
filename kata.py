def comp(array1, array2):
    if len(array1) != len(array2):
        return False
    if array1 == None and array2 == None:
        return True
    else:
        for i, v in enumerate(array1):

            for k in array2 : 
                if v == k:
                    break
                elif v ** 2  == k :
                    break
                elif v == k ** 2:
                    break
            else: 
                return False
    return True
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
result = comp(a1,a2)
print(result)