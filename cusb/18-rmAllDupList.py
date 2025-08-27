art = (
'''
┬─┐┌─┐┌┬┐┌─┐┬  ┬┌─┐      
├┬┘├┤ ││││ │└┐┌┘├┤       
┴└─└─┘┴ ┴└─┘ └┘ └─┘      
┌┬┐┬ ┬┌─┐┬  ┬┌─┐┌─┐┌┬┐┌─┐
 │││ │├─┘│  ││  ├─┤ │ ├┤ 
─┴┘└─┘┴  ┴─┘┴└─┘┴ ┴ ┴ └─┘
┬  ┬┌─┐┌┬┐               
│  │└─┐ │                
┴─┘┴└─┘ ┴                
'''

)



myli = input("Enter your desired list and seperate them with space : ").split()
# split() use to split the data as a list or dict

# print(myli)               for testing purposes

woRep = []

for i in myli:
    if i not in woRep:
        woRep.append(i)

print("list without removing duplicates : " , myli)
print("list with removing duplicates : " , woRep)
