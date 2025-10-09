f = open("demo.txt")
text = f.read()
lines = 0
words = 0
character = 0
#print(f.readline())
lines = text.split("\n")
words = text.split()
chars = len(text)
f.close()

print("The number of lines in demo.txt file : " , len(lines))

print("The number of words in demo.txt file : " , len(words))

print("The number of char in the demo.txt file : " , chars)
