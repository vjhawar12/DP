# function that returns the number of ways to get to the bottom right corner in an m * n grid
# if you start at the top left corner


def main(m, n, dic={}):
    if (m, n) in dic:
        return dic[(m, n)]
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1: 
        return 1
    dic[(m, n)] = main(m - 1, n, dic) + main(m, n - 1, dic)
    return dic[(m, n)]


print(main(18, 18))