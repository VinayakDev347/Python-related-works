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

#13) Create simple calculator

"""
print("\n***********************************\n Welcome to Simple Calculator!!!\n*********************************** \n")
num1 = int(input("Enter Your First Number :- "))
num2 = int(input("Enter your Second Number :- "))

Addition = num1 + num2
Substraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2
Fdivision = num1//num2
Exponent = num1**num2
Modules = num1 % num2

print(f"Addition: {num1} + {num2} is {Addition}")
print(f"Substraction: {num1} - {num2} is {Substraction}")
print(f"Multiplication: {num1} X {num2} is {Multiplication}")
print(f"Division: {num1} / {num2} is {Division}")
print(f"FloorDivision: {num1}//{num2} is {Fdivision}")
print(f"Remainder: {num1}%{num2} is {Modules}")
print(f"Exponentiation:{num1}**{num2} is {Exponent}")
print("***********************************")
print("ThankYou!!!")
"""

#14) Number comparison tool
"""
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
print("---------------------------------------------------")

if num1 == num2:
    print(f"Numbers are same {num1}")
elif num1 > num2:
    print(f"{num1} is greater than {num2} ")
else:
    print(f"{num1} is less than {num2}")
print("---------------------------------------------------")
if num1 ==0 or num2 == 0:
    print("one number you entered is 0")
else:
    print("entered Two input is zero")
"""

#15) create countdown timer 
"""
import time

start = int(input("Enter the number to start the countdown from: "))

print("\n--------------Countdown Begins--------------")
while start > 0:
    print(start)
    time.sleep(1)       #take 1sec gap
    start -= 1
print("--------------Countdown completed!!!--------------")
"""

#16) Basic Math Quiz game 
import random 

def generate_q():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = random.choice(['+','-','*'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return f"{num1} {operator} {num2}",answer

def math_quiz():
    score = 0 
    rounds = 5
    print("--------------Welcome to Math Quizz--------------")

    for i in range(rounds):
        questions, correct_answer = generate_q()
        print(f"\nQuestion {i + 1} : {questions}")
        user_answer = int(input("Your Answer: "))

        if user_answer == correct_answer:
            print("Correct Answer!!")
            score += 1
        else:
            print(f"Wrong Answer! The correct answer is : {correct_answer}")

    print("\n--------------Game Over--------------")
    print(f"Your final score is : {score}/{rounds} ")
    if score == rounds:
        print("Congratulations! You got  all the question Right") 
    elif score >= rounds//2:
        print("Good Job! Yor did it")
    else:
        print("Keep practicing! You can do better next time.")

math_quiz()