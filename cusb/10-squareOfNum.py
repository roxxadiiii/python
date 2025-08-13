art = (
'''
┌─┐┌─┐ ┬ ┬┌─┐┬─┐┌─┐
└─┐│─┼┐│ │├─┤├┬┘├┤ 
└─┘└─┘└└─┘┴ ┴┴└─└─┘
┌─┐┌─┐             
│ │├┤              
└─┘└               
┌┐┌┬ ┬┌┬┐          
││││ ││││          
┘└┘└─┘┴ ┴
'''
)

print(art)
num = int(input("Enter your desired number : "))

for i in range(1,num):
    sq = i * i
    print(sq)
