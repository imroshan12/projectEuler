sumOfMultiples = 0
n = int(input().strip())
n15 = (n-1)//15
n3 = (n-1)//3
n5 = (n-1)//5
sum5 = (n5/2)*(10 + (n5-1)*5)
sum3 = (n3/2)*(6 + (n3-1)*3)
sum15 = (n15/2)*(30 + (n15-1)*15)
sumOfMultiples = sum3 + sum5 - sum15
print(int(sumOfMultiples))
# sumOfMultiples = 0