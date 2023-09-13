def canConstruct(target, wordBank, dic={}):
    if target in dic: 
        return dic[target]
    if target == '':
        return True
    
    for i in wordBank:
        if i in target: 
            sliced = target.replace(i, '')
            if canConstruct(sliced, wordBank, dic):
                print(sliced)
                dic[sliced] = True
                return True

    dic[target] = False            
    return False


# print(canConstruct("hello", ['h', 'e', 'l', 'o']))
# print(canConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))