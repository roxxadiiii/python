# TypeBasedOverloading.py
art ="""
╔╦╗┬ ┬┌─┐┌─┐
 ║ └┬┘├─┘├┤
 ╩  ┴ ┴  └─┘
╔╗ ┌─┐┌─┐┌─┐┌┬┐
╠╩╗├─┤└─┐├┤  ││
╚═╝┴ ┴└─┘└─┘─┴┘
╔═╗┬  ┬┌─┐┬─┐┬  ┌─┐┌─┐┌┬┐┬┌┐┌┌─┐
║ ║└┐┌┘├┤ ├┬┘│  │ │├─┤ │││││││ ┬
╚═╝ └┘ └─┘┴└─┴─┘└─┘┴ ┴─┴┘┴┘└┘└─┘
"""

print(art)

# Create a method that performs different operations based on argument types (e.g. Multiply if both are ints , repeat if first is string and second is int) - TypeBasedOverloading.py

# creating a class for operations
class Operation:
    def perform(self, p , q):
        if isinstance(p,int) and isinstance(q,int):
            return p * q
        elif isinstance(p,str) and isinstance(q,int):
            return p * q
        elif isinstance(p,int) and isinstance(q,str):
            return p * q
        else:
            return "Unsupported input"


op = Operation()


val1 = input("Enter the first value : ")
val2 = input("Enter the second value : ")


## Convert inputs to integers if possible
try:
    val1 = int(val1)
except ValueError:
    pass
try:
    val2 = int(val2)
except ValueError:
    pass


print(op.perform(val1,val2))
