# write a program that determines if a target sum can be generated using numbers from an inputted array

# def canSum(target, nums):
#     if target < 0:
#         return False
#     if target == 0:
#         return True
    
#     for i in nums:
#         if canSum(target - i, nums):
#             return True
        
#     return False 

def canSum(target, nums, dic={}):
    if target < 0:
        return False
    if target == 0: 
        return True
    if target in dic:
        return dic[target]

    for i in nums:
        dic[target] = canSum(target - i, nums, dic)
        if dic[target] == True:
            return True

    return False


print(canSum(7, [2, 3], {}))
print(canSum(7, [5, 3, 4, 7], {}))
print(canSum(7, [2, 4], {}))
print(canSum(8, [2, 3, 5], {}))
print(canSum(300, [7, 14], {}))

    
