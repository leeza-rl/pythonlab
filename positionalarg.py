# 1. basic positional argumrnts
def add(a,b):
    print("a= ",a)
    print("b= ",b)
    return a+b

result=add(10,30)
print("sum= ",result)

#student information
def student_info(name,roll,marks):
    print("name: ",name)
    print("roll:",roll)
    print("marks: ",marks)
    
student_info("leeza",5,90)

# simple interest
def simple_intrest(p,r,n):
    si=(p*r*n)/100
    print("simple intsert: ",si)
simple_intrest(100,2,2)
simple_intrest(50000,1.2,3)

# area of circle
def ar_circle(r):
    ar_circle=3.14*r*r
    print("area of : ",ar_circle)
ar_circle(1.5)
ar_circle(5)

# check no. positve, negaive or zero
def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
check_value(0)
check_value(50)
check_value(-2)

# add or even
def odd_even(no):
    if(no%2==0):
        print("value is even")
    else:
        print("value is odd")
odd_even(50)
odd_even(45)

# arithmetic operation substraction,multiplication and divison
def addtion(a,b):
    add=a+b
    print("addtion of two values",add)
addtion(56,26)
addtion(100,50.0)