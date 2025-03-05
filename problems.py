#lastDigit&Divisibility
n = 3456
while (n>0):
    ld = n%10
    print(ld)
    n=n//10

#countOfDigitInNumber
n = 234567
c = 0
while (n>0):
    c = c + 1
    n //= 10
print(c)

#oddDigit
n = 23456
c = 0
while (n>0):
    ld = n%10
    if (ld%2==0):
        c = c+1
        n = n//10
print(c)
