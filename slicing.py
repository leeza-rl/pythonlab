#basic slices

from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])
array('i', [20, 30, 40])
print(arr[:3])
array('i', [10, 20, 30])
print(arr[2:])
array('i', [30, 40, 50])
print(arr[:])
array('i', [10, 20, 30, 40, 50])

#slicing with step
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])
array('i', [10, 30, 50, 70])
print(arr[1::2])
array('i', [20, 40, 60, 80])
print(arr[::3])
array('i', [10, 40, 70])

#negative slicing

arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])
array('i', [20, 30, 40])
print(arr[-3])
30
print(arr[-3:])
array('i', [30, 40, 50])
print(arr[:-2])
array('i', [10, 20, 30])

#reverse array using slicing
arr= array('i',[10,20,30,40,50])
print(arr[::-1])
array('i', [50, 40, 30, 20, 10])

