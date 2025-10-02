art = """
┬  ┌─┐┌┐┌
│  ├┤ │││
┴─┘└─┘┘└┘
╔═╗┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌
╠╣ │ │││││   │ ││ ││││
╚  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘
"""


print(art)


"""

len() is a built-in Python function that returns the number of items in an object.

It works on sequences (strings, lists, tuples) and collections (sets, dictionaries).

For strings, len() counts the number of characters.

For lists, tuples, and sets, len() counts the number of elements.

For dictionaries, len() counts the number of key-value pairs.

It does not work on integers or floats directly (unsupported types).
"""
a = " : "

# String
text = "Python"
print(text ,a, len(text))

# output
# Python 6



# list
nums = [10, 20, 30, 40]
print(nums ,a, len(nums))

# output
# [10, 20, 30, 40]  :  4



# tuple ;
t = (1, 2, 3, 4, 5)
print(t,a,len(t))


# output
# (1, 2, 3, 4, 5)  :  5



# set ;
s = {1, 2, 3, 4}
print(s , a, len(s))

# output
# {1, 2, 3, 4}  :  4
