"""
type() is a built-in Python function used to find the type (class) of an object.

It tells what kind of data (string, list, int, float, etc.) the object belongs to.

Useful for debugging, validation, and understanding how Python treats different values.

The return value of type() itself is a type object (like <class 'str'>, <class 'list'>).

Objects of the same type can usually be combined, manipulated, or iterated in similar ways.
"""

# for String

text = "Python"
print("text = " , text , type(text))
# output should be like
# <class 'str'>




# for int
num = 42
print("num = " , num , type(num))
# output
#<class 'int'>



# for list
numbers = [1, 2, 3]
print("list = " , numbers , type(numbers))
# output
#<class 'list'>


# for float
pi = 3.14
print("float = " , pi , type(pi))
# output
# <class 'float'>



# for tuple
coords = (10, 20)
print("coords = " , coords , type(coords))
# output
#<class 'tuple'>
