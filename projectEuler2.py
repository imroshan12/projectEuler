#!/bin/python3

import sys
def evenFiboSum(n):
    fn_2 = 2
    fn_1 = 8
    sum = 10
    while True:
        fn = 4*fn_1 + fn_2
        if fn > n:
            return sum
        sum += fn
        fn_2, fn_1 = fn_1, fn


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(evenFiboSum(n))









    # Lengthy Solution


    # import sys
    # fiboSum = 2
    # fibosequence = [1,2]
    # n = int(input().strip())
    # for i in range(2,n):
    #     fibosequence.append(fibosequence[i-2] + fibosequence[i-1])
    #     # print(fibosequence[i])
    #     if fibosequence[i] <= n:
    #         if fibosequence[i]%2 == 0:
    #             fiboSum += fibosequence[i]
    # print(fiboSum)
