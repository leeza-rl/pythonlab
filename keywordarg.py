# basic keyword argumentd
def student_info(name,age,city):
    print("name: ",name)
    print("age: ",age)
    print("city: ",city)
    
student_info(age=18,city="rajkot",name="leeza")

# mixing positional and keyword
def display(a,b,c):
    print("a= ",a)
    print("b= ",b)
    print("c= ",c)
    
display(1,c=6,b=7)