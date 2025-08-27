art = (
'''

┬─┐┌─┐┬  ┬┌─┐┬─┐┌─┐┌─┐
├┬┘├┤ └┐┌┘├┤ ├┬┘└─┐├┤ 
┴└─└─┘ └┘ └─┘┴└─└─┘└─┘
┬ ┬┬┌┬┐┬ ┬┌─┐┬ ┬┌┬┐   
││││ │ ├─┤│ ││ │ │    
└┴┘┴ ┴ ┴ ┴└─┘└─┘ ┴    
┌─┐┬  ┬┌─┐┬┌┐┌┌─┐     
└─┐│  ││  │││││ ┬     
└─┘┴─┘┴└─┘┴┘└┘└─┘     
 ┌─┐┬ ┬               
 ├─┘└┬┘               
o┴   ┴                
'''

)


print(art)
s = input("Enter your desired string : ")

rs = " "

for i in s:
    rs = i + rs

# hence reversed string

print("reversed string is : " , rs)
