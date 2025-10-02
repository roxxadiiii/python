art ="""
╔╦╗┬ ┬┌─┐┌─┐┌─┐┌─┐┌─┐┌┬┐┬┌┐┌┌─┐
 ║ └┬┘├─┘├┤ │  ├─┤└─┐ │ │││││ ┬
 ╩  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴┘└┘└─┘

"""

print(art)

"""
Typecasting means converting one data type into another in Python.

It is done using constructor functions like int(), float(), str(), list(), tuple(), etc.

Typecasting is required when you want to perform operations that need specific types (e.g., arithmetic on numbers instead of strings).

Some conversions are safe and natural (e.g., int("10") → 10), while others may raise errors (e.g., int("abc") → error).

Typecasting always creates a new object of the target type; the original object remains unchanged.
"""

# String -> Integer
s = "123"
num = int(s)
print(num, type(num))

# output
# 123 <class 'int'>



# String -> float
s = "3.14"
pi = float(s)
print(pi, type(pi))

# output
#3.14 <class 'float'>


#Integer -> String
n = 42
s = str(n)
print(s, type(s))


# output
# 42 <class 'str'>


# List -> tuple

lst = [1, 2, 3]
t = tuple(lst)
print(t, type(t))

# output
# (1, 2, 3) <class 'tuple'>


# tuple -> list

t = (4, 5, 6)
lst = list(t)
print(lst, type(lst))


# output
# [4, 5, 6] <class 'list'>



# number -> complex
n = 5
c = complex(n)
print(c, type(c))

# output
# (5+0j) <class 'complex'>
