

# Questions By university

[ x ] 1.Print sum of the digits of the given number..
```
#!/usr/bin/env python3

num = input("Enter a desired 4 digits number : ")



sum = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])


print("sum of the digits is : " , sum)

```
[ x ] 2.Swap two given number with the help of a third variable and print it respectively.
```
#!/usr/bin/env python3

A = int(input("enter A : "))
B = int(input("enter B : "))

temp = A
A = B 
B = temp

print("the new A is : " , A)
print("the new B is : " , B)

```
[ x ] 3.check the number if it is even or odd.
```
#!/usr/bin/env python3

number = int(input("enter the desired number : "))

if number % 2 == 0:
                print(number," is even")

else:
                   print(number,"is odd")

```
[ x ] 4.take three numbers and print the greatest among all three.
```
#!/usr/bin/env python3

A = int(input("enter A : "))
B = int(input("enter B : "))
C = int(input("enter C : "))



if A > B and A > C :
    print("A is greatest")

elif B > A and B > C :
    print("B is greatest")

elif B == A and C == A:
    print("A , B and C are same")

else:
#elif C > A and C > B:
    print("C is greatest")

```
[ x ] 5.reverse a string without a loop.
```
#!/usr/bin/env python3

string = input("Enter a desired 5 character String : ")

at5 = string[0]
at4 = string[1]
at3 = string[2]
at2 = string[3]
at1 = string[4]


reversed = at1 + at2 + at3 + at4 + at5

print(reversed)

```
[ x ] 6.count the number of digits .
```
#!/usr/bin/env python3
s = input("Enter a desired string of any length : ")

rs = s[::-1]

print("reversed string is : " + rs)

```
[ x ] 7.find the Greatest Common Divisor HCF of two numbers .
```
#!/usr/bin/env python3

test = "jhwvekjbcehkvw"
s = input("Enter the desired string for the length : ")



print("length of the desired string is : " , len(s))

```
[ x ] 8.find the LCM of the two number .
```
#!/usr/bin/env python3

print(
'''
 ██████╗██╗██████╗  ██████╗██╗     ███████╗
██╔════╝██║██╔══██╗██╔════╝██║     ██╔════╝
██║     ██║██████╔╝██║     ██║     █████╗  
██║     ██║██╔══██╗██║     ██║     ██╔══╝  
╚██████╗██║██║  ██║╚██████╗███████╗███████╗
 ╚═════╝╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝
                                           

'''
        )

r = float(input("enter the radius for the circle (in m): "))

area = 3.147 * r * r 

circumference = 2 * 3.147 * r 

print("area of the circle is : " , area , "m sq.")
print("circumference of the circle is : " , circumference , "m")

```
[ x ] 9.factorial using recursion .
```
#!/usr/bin/env python3

art = (
'''

┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐   
││││ ││││├┴┐├┤ ├┬┘   
┘└┘└─┘┴ ┴└─┘└─┘┴└─   
┌┬┐┬ ┬┬ ┌┬┐┬┌─┐┬  ┌─┐
││││ ││  │ │├─┘│  ├┤ 
┴ ┴└─┘┴─┘┴ ┴┴  ┴─┘└─┘
'''
)

print(art)
num = input("Enter the desired number to print the table : ")

for i in range(1,11):
    multiple = int(num) * i
    print(multiple)

```
[ x ] 10.area and circumference of a circle .
```
#!/usr/bin/env python3
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

```
[ x ] 11.area and perimeter of a rectangle . 
```
#!/usr/bin/env python3
art = (
'''
  __   _          __  ___               
 /_ | | |        /_ |/ _ \              
  | | | |_ ___    | | | | |             
  | | | __/ _ \   | | | | |             
  | | | || (_) |  | | |_| |             
  |_|  \__\___/   |_|\___/              
                       | |              
  _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | | | | |_| | | | | | | |_) |  __/ |   
 |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                        

'''
)

print(art)

for i in range(1,11):
    print(i)
```
[ x ] 12.write a python program to print the table of a given number.
```
#!/usr/bin/env python3

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

```
[ x ] 13.write a program that prints the squares of all the numbers less than or equal to a given number .
[ x ] 14.write a python program that prints number from 1 to 10.
[ x ] 15.write a python program to calculate the factorial of a number using a for loop .
[ x ] 16.write a program to find if a given number os prime or not.
[  ] 17.write a python program to print the fibonacci sequence up to n terms , where n is input by the user.
[  ] 18.write a python program to generate the fibonacci series with a given number of elements .
[  ] 19.write a python program to check whether a given (input from user) string or number is a palindrome .
[  ] 20.write a python function that counts the numbers of vowels in a given string .
[  ] 21.write a python program to reverse a given string without using slicing .
[ x ] 22.Write a python program to remove all duplicates from a given list .
[  ] 23.Write a python function find_max_min that returns maximum and minimum values in a list .
[  ] 24.Write a python program to count the frequency of each word in a given text .
[  ] 25.Write a python function that takes a dictionary as input and returns the key with the highest value .
[  ] 26.Write a Python function that accepts an arbitrary number of keyword arguments and prints the result as a dictionary .
[ x ] 27.Write a Python function is prime that checks if a number is a prime number .
[  ] 28.Write a python function that accepts an arbitrary number of keyboard arguments and prints the result as a dictionary .
[  ] 29.Write a python program that takes a list of integers and returns a new list that contains only the even numbers using list comprehensions .
[  ] 30.Write a pyhton list comprehension to generate a list of squares of numbers between 1 and 10 .
[  ] 31.Write a python program to read text file and print the number of lines .
[  ] 32.Write a python program to write the contents of one file into another file .
[  ] 33.write a program that finds a string in a given file .
[  ] 34.Write a program that finds a given string in a file and returns the place where the string appears in the file . your program should return the index of the first character of the given string in the file .
