# Ex.1
def greet(name="GUEST"):
    print("Hellooooo",name)
    
greet("Leeza")
greet()

# sum
def add(a,b=5):
    print("sum",a+b)
    
add(30,50)
add(90)

# squere number
def sqr(num,exp=2):
    return num**exp

print(sqr(3))
print(sqr(3,3))
print(sqr(2,4))