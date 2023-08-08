#Printing first three characters of a string

word = input()
word = word[0 : 3]
print(word)

#part of a string 

word = input()
index = int(input())

result = word[index: ]
print(result)

#Printing last n characters 

word = input()
num = int(input())
word_length = len(word)

start_index = word_length - num 
part = word[start_index: ]
print(part)

#half string 

word= input()
length = len(word)
index = int(length/2)
part = word[ : index]
print(part)

#Replace a letter 

W = input()
I = int(input())
C = input()

first_part = W[0: I]
last_part = W[I+1 : ]

result = first_part + C + last_part
print(result)