# basic try-except
"""
try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    result = number1 / number2
    
except ZeroDivisionError:
    print("you cannot dived by zero!")

except ValueError:
    print("Please enter a valid number!")
    
else:
    print("Divison successfull Result is: ",result)
    
finally:
    print("This block always runs.") """
    
try:
    my_list = [1,2,3]
    print(my_list[2])
    
except IndexError:
    print("Index is out of range!")
    
else:
    print("Element found successfully!")
    
finally:
    print("Program finished.")