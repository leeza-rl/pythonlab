#1.print message
x = "Welcome To Atmiya"
print(x)

#2.add two numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("sum = ",a+b)

#3.check even ar odd
n = int(input("Enter a Number: "))

if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#4.check leap year
year = int(input("Enter Year: "))

if (year % 400 == 0):
    print("leap Year")
else:
    print("Not a Leap Year")

#5.print PI value
import math
print("PI value = ",math.pi)

#6.store and print constant value
PI = 3.14
print("Constant Value PI : ",PI)

#7.square of a number
n = int(input("Enter a number: "))
print("Square =",n*n)

#8.area of circle
import math
r = float(input("Enter radius: "))
area = math.pi * r * r
print("Area of circle = ",area)

#9.check data type
a = 10
b = 5.5
c = "python"

print(type(a))
print(type(b))
print(type(c))

#10.use math functions
import math
print("Square root of 25 = ",math.sqrt(25))
print("Factorial of 5 = ",math.factorial(5))
print("Power 2^3 = ",math.pow(2,3))

#11.find power
a = int(input("Enter Base : "))
b = int(input("Enter Exponent : "))

print("Power = ",a ** b)

#12.check positive or negative
n = int(input("Enter a number: "))

if n > 0:
    print("Positive Number")
elif n < 0:
    print("Negative Number")
else:
    print("Zero")


