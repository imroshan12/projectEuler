t = int(input())
for i in range(t):
    n = int(input())
    number = 2 ** n
    sumOfDigits = 0
    for digit in str(number):
        sumOfDigits += int(digit)
    print(sumOfDigits)
