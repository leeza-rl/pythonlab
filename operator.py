#1.ARITHMETIC OPERATORS
# addition
a = 5
b = 6
print(a+b)

# subtraction
print(a-b)

# multiplication
print(a*b)

#division
print(a/b)

#modulus
print(a%b)

#floor division
print(a//b)

#power
print(a**b)

#2.RELATIONAL OPERATORS
#equal
a = 5
b = 8
print(a==b)

#not equal
print(a!=b)

#greater than
print(a>b)

# less than
print(a<b)

# greater or equal
print(a>=b)

# less or equal
print(a<=b)


#3.LOGICAL OPERATORS
#and
a = 5
print(a>2 and a<10)

# or
a = 5 
print(a>5 or a<3)

# not
a = 5
print(not a>5 )

#4.ASSIGNMENT OPERATORS
a = 5
print(a)

a = 5
a += 2
print(a)

a = 5
a -= 2
print(a)

a = 5
a *= 2
print(a)

#5.BITWISE OPERATORS
#and 
a = 5
b = 7
print(a&b)

# or
print(a*b)

#not
print(~b)

#left shift
print(a<<b)

# right shift
print(a>>b)

#6.MEMBERSHIP OPERATPRS
# in
a = ('sakshi','dhruvi','priyanshi')
print('a' in 'sakshi')

#not in
print('z' not in 'sakshi')

#7.IDENTITY OPERATORS
#is
a = 5
b = 5
print(a is b)

#is not
a = 5
b = 8
print(a is not b)

# 8.CONDITIONAL OPERATORS
a = 10
result = "even"if a % 2==0 else "odd"
print(result)

#9.UNARY OPERATORS
#unary plus
a = 5
print(+a)

#unary minus
print(-a)

#unary not (bitwise NOT)
print(~a)