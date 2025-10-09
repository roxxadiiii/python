art = '''
┌─┐┬ ┬┌─┐┌─┐┌─┐┬┌┐┌┌─┐
└─┐│││├─┤├─┘├─┘│││││ ┬
└─┘└┴┘┴ ┴┴  ┴  ┴┘└┘└─┘
┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐┌─┐
││││ ││││├┴┐├┤ ├┬┘└─┐
┘└┘└─┘┴ ┴└─┘└─┘┴└─└─┘
'''


print(art)

a =input("a : ")
b =input("b : ")

# temp Value

temp = a
a = b
b = temp

# printing

print("value of a after swapping : ",a)
print("value of b after swapping : ",b)


# output
'''
a : 123
b : 121233
value of a after swapping :  121233
value of b after swapping :  123

'''
