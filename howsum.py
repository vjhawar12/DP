# write a program that returns how a target sum can be generated using numbers from an inputted array

def howsum(target, nums, dic={}):
    if target == 0:
        return []
    if target < 0:
        return None
    if target in dic:
        return dic[target]
    
    for i in nums:
        result = howsum(target - i, nums, dic)
        
        if result is not None:
            result.append(i)
            dic[target] = result
            return result
    
    dic[target] = None
    return None

print(howsum(7, [2, 3], {}))
print(howsum(7, [5, 3, 4, 7], {}))
print(howsum(7, [2, 4], {}))
print(howsum(8, [2, 3, 5], {}))
print(howsum(300, [7, 14], {}))


