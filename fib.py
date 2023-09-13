from time import time

def fib(n, dic={}): 
    if n in dic: return dic[n]
    if n < 2: return n
    dic[n] = fib(n - 2, dic) + fib(n - 1, dic)
    return dic[n]
    
print(fib(1150))
  



