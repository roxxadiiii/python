art="""
╦┌┐┌┌─┐┬ ┬┌┬┐
║│││├─┘│ │ │
╩┘└┘┴  └─┘ ┴
╔═╗┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌
╠╣ │ │││││   │ ││ ││││
╚  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘
"""

print(art)
"""
input() is a built-in Python function used to take user input from the keyboard.

It always returns the entered data as a string, no matter what the user types.

If you need another type (like int or float), you must convert the result using functions like int() or float().

It pauses program execution until the user presses Enter.

Useful for interactive programs where user input is required.
"""

# String
name = input("Enter your name: ")
print("Hello,", name)
print(type(name))

# Converting Inputing to Integers ;
age = int(input("Enter your age: "))
print("You are", age, "years old")
print(type(age))

# Converting input to float ;

pi_val = float(input("Enter value of pi: "))
print("Pi is approx:", pi_val)
print(type(pi_val))


# mix with other

print("Hello " + input("What is your name ???? "))
