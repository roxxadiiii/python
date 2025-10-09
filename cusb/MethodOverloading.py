art ='''
╔╦╗┌─┐┌┬┐┬ ┬┌─┐┌┬┐
║║║├┤  │ ├─┤│ │ ││
╩ ╩└─┘ ┴ ┴ ┴└─┘─┴┘
╔═╗┬  ┬┌─┐┬─┐┬  ┌─┐┌─┐┌┬┐┬┌┐┌┌─┐
║ ║└┐┌┘├┤ ├┬┘│  │ │├─┤ │││││││ ┬
╚═╝ └┘ └─┘┴└─┴─┘└─┘┴ ┴─┴┘┴┘└┘└─┘
╔═╗┬┌┬┐┬ ┬┬  ┌─┐┌┬┐┬┌┐┌┌─┐
╚═╗│││││ ││  ├─┤ │ │││││ ┬
╚═╝┴┴ ┴└─┘┴─┘┴ ┴ ┴ ┴┘└┘└─┘
'''

print(art)

# creating a class
class Calculator:
    def add(self,*args):                            # defining a function to take arguments
        # CASE 1 : printing if nonumbered entered
        if len(args) == 0:
            return "No Numbered Provided"
        # CASE 2 : printing one numbered if and only one numbered is provided
        elif len(args) == 1:
            return args[0]
        # CASE 3 :if input numbered is greated than 2
        else:
            return sum(args)


# Create an object of Calculator
calc = Calculator()




num = input("Enter the numbers with a space : ").split()
num =[float(a) for a in num]

print(calc.add(*num))
