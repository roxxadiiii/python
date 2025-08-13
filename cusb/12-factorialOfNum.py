art = (
'''
┌─┐┌─┐┌─┐┌┬┐┌─┐┬─┐┬┌─┐┬  
├┤ ├─┤│   │ │ │├┬┘│├─┤│  
└  ┴ ┴└─┘ ┴ └─┘┴└─┴┴ ┴┴─┘
┌─┐┌─┐                   
│ │├┤                    
└─┘└                     
┌┐┌┬ ┬┌┬┐                
││││ ││││                
┘└┘└─┘┴ ┴
'''
)

print(art)

num = int(input("Enter the desired number to calculate factorial : "))

for i in range(1,num):
    num = num * i

print(num)
