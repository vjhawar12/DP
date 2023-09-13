# write a program that returns how a target sum can be generated using the least number of numbers 
# numbers possible from an inputted array

def bestsum(target, nums, dic):
    if target in dic:
        return dic[target]
    if target == 0:
        return []
    if target < 0:
        return None
    
    shortest = None
    for i in nums:
        result = bestsum(target - i, nums, dic)
        if result != None:
            result.append(i)
            if shortest == None or len(result) < len(shortest): 
                shortest = result
    
    dic[target] = shortest
    return shortest

print(bestsum(10, [2, 5], {}))
print(bestsum(7, [2, 3], {}))
print(bestsum(7, [5, 3, 4, 7], {}))
print(bestsum(7, [2, 4], {}))
print(bestsum(8, [2, 3, 5], {}))
print(bestsum(300, [7, 14], {}))

