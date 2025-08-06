#1) write a program to find the largest number from the list

"""
num = [1,2,9,3,4,5]
max = num[0]
for i in num:
    if i > max:
        max = i
print(max)
"""
      
#2) write a program to remove duplicates from the given list
"""
list1 = [1,2,2,3,4,5,5,6,5,3]
# newlist = set(list1)              #----> set didnot allow duplicates
# print(newlist)
new = []
for i in list1:
    if i not in new:
        new.append(i)
print(new)

"""

#3) change message to emoji
"""
# message = input("> ")
# words = message.split(' ')
# print(words)
# emojis = {                          # Windos key + .
#     ":)":"😁",
#     ":(":"😔"
# }
# output = ''
# for word in words:
#     output += emojis.get(word,word) + " "
# print(output)

"""

#4) Examples for OOPs - Inheritance
"""
class Pets:
    def Walk(self):
        print("walk")

class Dog(Pets):
    def Bark(self):
        print("Barking Dogs!!!")

class Cat(Pets):
    def be_annoying(self):
        print("be_annoying!!!")

cat1 = Cat()
cat1.Walk()
dog1 = Dog()
dog1.Walk()
"""

#5) Mark Even or odd
"""
num = int(input("Enter a number to check the number is even or odd: "))
if num == 0:
    print(f"The Number is {num},take it also as even")
elif num % 2 == 0:
    print(f"The Given Number {num} is Even")
else:
    print(f"The Number {num} is odd")
"""

#6) Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
"""
def checking(a,b,flag):
    if flag == False:
        if ( a>= 0 and b <0) or (a < 0 and b >= 0):
            return True
    else:
        if a < 0 and b <0:
            return True
    return False

print(checking(2,4,False))
"""

#7) Using list comprehension write code for finding square from 0 to 10 
"""
li = [i*i for i in range(11)]
print(li)
"""

#8) Write a function which would divide two numbers, design the function in a manner that it handles the divide  by zero exception

"""
def checking(num1,num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error Occured...cannot divide by 0"
    
print(checking(11,0))       #error occure here
"""

#9) Write Python code to open a file named  demo.txt and write some random data into it.

"""
with open("demo.txt","w") as file:
    file.write("Datas are Here guyzz....")

#10) Open the file,read  the contents and display them as output.

with open("demo.txt","r") as file:
    contents = file.read()
    print(contents)

#11) Write python code to add  additional text to the excisting  file on a new line  without deleting the previous contents

with open("demo.txt","a") as file:
    file.write("This is the additional text's")
    
    #checking the datas are added or not!
with open("demo.txt","r") as file:
    contents = file.read()
    print(contents)
"""

#12) Create a number guessing game 
"""
import random as rd

secreat_no = rd.randint(1,10)
attempts = 3

while attempts > 0:
    guess = int(input("Take a Guess, Between 1 to 10 :- "))
    if guess == secreat_no:
        print("You Guessed Correctly!!!")
        break
    elif guess < secreat_no:
        print("Your Guess is Low ,Try Again...:- ")
    else:
        print("Your Guess is high ,Try Again...:- ")
    attempts -= 1

if attempts == 0:
    print("Your attempts is over Your Failed!!! \n Secreat Number is : ",secreat_no)
"""
    