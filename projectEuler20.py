t = int(input())
for _ in range(t):
    n = int(input())
    fact = 1
    sumOfDigits = 0
    for i in range(2, n+1):
        fact *= i
    for digit in str(fact):
        sumOfDigits += int(digit)
    print(sumOfDigits)