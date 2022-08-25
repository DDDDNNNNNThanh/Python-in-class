# Dương Nhật Thành

# 11219287

# DSEB 63

# Ex1:

import math
def f(x):
    return 1/x
n = int(input("enter n(even numbers) = "))
a = int(input("enter a = "))
b = int(input("enter b = "))
dx = (b-a)/n
s = 0
for i in range(1,(n//2+1)):
    s += dx/3*(f(a+(2*i-2)*dx) + 4*f(a+(2*i-1)*dx) + f(a+2*i*dx))
print(f"result = {s}")
error = math.log(b) - math.log(a) - s
print(f"error = {error}")


# Ex2:

card_number = input("Please input card number:")
digits = [int(d) for d in card_number]
last_digit = digits[-1]
new_digits = digits[:-1]
odd_digits = new_digits[-1::-2]
even_digits = new_digits[-2::-2]
print(odd_digits)
checksum = 0
checksum += sum(even_digits)
for d in odd_digits:
    d = d * 2
    if d >= 10:
        d = d - 9
    checksum += d
check_digit = 10 - (checksum%10)
print('Valid') if check_digit==last_digit else print('Invalid')


# Ex3:

x = int(input("Please enter x ="))
n = int(input("Please enter n ="))
sum = 0
for i in range(1,n+1):
    sum += i*(x**(i-1))
print(sum)


# Ex4:

x = int(input("Please enter x="))
y = int(input("Please enter y="))
A = x**2+4*x+y**2+7*x-5
print(A)






