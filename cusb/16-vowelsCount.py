art = (
'''
┬  ┬┌─┐┬ ┬┌─┐┬  ┌─┐   ┌─┐┌─┐┬ ┬┌┐┌┌┬┐┌─┐┬ ┬
└┐┌┘│ ││││├┤ │  └─┐───│  │ ││ ││││ │ ├─┘└┬┘
 └┘ └─┘└┴┘└─┘┴─┘└─┘   └─┘└─┘└─┘┘└┘ ┴o┴   ┴ 

'''

)

print(art)

# real code begins

s = input("Enter the desired string : ")
vowels = "aeiouAEIOU"
lenS = len(s) - 1
count = 0
for char in s:
    if char in vowels:
        count = count + 1
print("the numbers of vowels : " , count)
