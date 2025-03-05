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
n = 7654322
c = 0
while (n>0):
    ld = n%10
    if (ld%2!=0):
        c=c+1
    n = n // 10
print(c)

#power&kthDigitFromLast
a = 8
b = 3
c = 1
d = 1
for i in range(1,b+1):
    d = d*a
s = 0
print(d)
while (d>0):
    l=d%10
    s=s+1
    if (s==c):
        print(l)
        break
    d=d//10
