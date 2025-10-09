'''
Variables in Python are names that store data values in memory.

They act as references or labels pointing to objects (numbers, strings, lists, etc.).

Python variables do not need explicit type declaration — the type is inferred from the assigned value.

A variable’s type can change if you assign a new value of a different type.

Variable names are case-sensitive (Name and name are different).

They must begin with a letter or underscore, and cannot start with a number.

Assignment is done using the equals sign =.

Multiple variables can be assigned in one line.
'''


art = """
┬  ┬┌─┐┬─┐┬┌─┐┌┐ ┬  ┌─┐┌─┐
└┐┌┘├─┤├┬┘│├─┤├┴┐│  ├┤ └─┐
 └┘ ┴ ┴┴└─┴┴ ┴└─┘┴─┘└─┘└─┘
"""


print(art)


x = 10
y = "Python"
print("x and y : " ,x, y)


# output x and y :  10 Python


a = 10
print("a : " , type(a))

# output
# a :  <class 'int'>


b = 100
b = "Now I’m a string"
print("b : " , b, type(b))

# output
# b :  Now I’m a string <class 'str'>

# multiple assigment
p, q, r = 1, 2, 3
print("p,q and r : ", p, q, r)

# output
# p,q and r :  1 2 3

# Same value to multiple variables
j = k = l = "Data"
print("value of j,k and l : ",j, k, l)

# output
# value of j,k and l :  Data Data Data

# Reassignment

n = 5
n = n + 2
print("n : " ,n)
# output
# n :  7

# with different types

name = "Alice"
age = 25
height = 5.4
is_student = True
print(name, age, height, is_student)
print("name : " ,type(name) , "age : ", type(age) , "height : " , type(height) , "is_student : " ,type(is_student))

# output
# Alice 25 5.4 True name :  <class 'str'> age :  <class 'int'> height :  <class 'float'> is_student :  <class 'bool'>

# lectures code
print(" \n \n \nlectures code ;")
nm =input("What is your name?? : ")
print("name : ", nm)
print("length of name : " ,len(nm))
# output

