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
"""
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
"""

#17) Shopping list app
"""
shopping_list = []

def show_menu():
    print("\n-------Shopping List Menu-------")
    print("1.View the shopping list")
    print("2.Add an Item")
    print("3.Remove an Item")
    print("4.Clear the list")
    print("5.Exit")

while True:
    show_menu()
    choice = int(input("Enter Your Choice 1 - 5: "))
    
    if choice == 1:
        print("\n----------shopping_list----------")
        if not shopping_list:
            print("Shopping List is empty....")
        else:
            for index,item in enumerate(shopping_list):
                print(f"{index+1}. {item} ")

    elif choice == 2:
        item = input("Enter Item To Add: ")
        shopping_list.append(item)
        print(f"{item} has been added to the Shopping List")
    
    elif choice == 3:
        item = input("Which item you want to remove?")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} was removed successfully")
        else:
            print(f"{item} not found in the list")

    elif choice == 4:
        shopping_list.clear()
        print("Shopping list was cleared successfully")

    elif choice == 5:
        print("Good Bye, Exited!!!")    
        break
    else:
        print("invalid choice,try again!")

show_menu()
"""

#18) Contact Book dictonaries
"""
contact_book = {}

def show_menu():
    print("\n***********Contact Book***********")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter Your Contact name: ")
    phone = input("Enter Your Contact Phone: ")
    email = input("Enter Your Contact Mail: ")
    contact_book[name] = {"phone":phone,"email":email}
    print(f"{name} has been added to your contact list")

def view_contact():
    if contact_book:
        print("\n---------Contact Book---------")
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"phone: {details['phone']}")
            print(f"email: {details['email']}")
    else:
        print("Your contact is empty!!!")

def search_contact():
    name = input("Enter the name of your contact you want to search")
    if name in contact_book:
        print(f"\n---------Contact detail of your {name}---------")
        print(f"Name: {name}")
        print(f"phone: {contact_book[name]['phone']}")
        print(f"email: {contact_book[name]['email']}")
    else:
        print(f"Contact {name} not found in your contact book.")

def edit_contact():
    name = input("Enter the name of your contact you want to Edit")
    if name in contact_book:
        phone = input("Enter Your Contact Phone: ")
        email = input("Enter Your Contact Mail: ")
        contact_book[name] = {"phone":phone,"email":email}
        print(f"Contact {name} has been updated successfully")
    else:
        print(f"Contact {name} not found in your contact book!!!")

def delete_contact():
    name = input("Enter the name of your contact you want to delete")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} has been deleted successfully")
    else:
        print(f"Contact {name} has not found in your contact book!!!")

while True:
    show_menu()
    choice = int(input("enter your choice (1-6): "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        edit_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("ThankYou for using Contact Book. Good Bye")
        break
    else:
        print("Invalid choice. please select valid options 1-6 ")
"""

#19) Ingredients checker 
"""
recipe_ingredients = {"flour" , "sugar" , "butter" , "eggs" , "milk"}

user_input = input("Enter the ingredients you have (seperated by comas): ")
user_ingredients = set(user_input.split(", "))

missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

print("-------ingredient Checker Result----------")
if missing_ingredients:
    print(f"You are missing the following ingredients: {','.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed")

if extra_ingredients:
    print(f"You have all the extra ingredients {",".join(extra_ingredients)}")
else:
    print("You have all the ingredients needed")
"""

#20) Note Taiking App 
"""
FILE_NAME= "MyTestNotes.txt"

def show_menu():
    print("----------Note TaIKING App----------")
    print("1. Add a new Note")
    print("2. View all Note")
    print("3. Delete all Note")
    print("4. Exit")


def add_note():
    note = input("Enter Your Note: ")
    with open(FILE_NAME,"a") as file:
        file.write(note+"\n")
    print("Note added successfully")


def view_all_note():
    try:
        with open(FILE_NAME,"r") as file:
            content = file.read()
            if content:
                print("\n -----All Notes-----")
                print(content)
            else:
                print("\nNo notes found")
    except FileNotFoundError:
        print("No notes Found")

def delete_notes():
    confirm = input("Are you sure you want to delete all your note? (y/n): ")
    if confirm.lower() == "y":
        with open(FILE_NAME,"w") as file:
            file.write("")
            pass
        print("All Note have been deleted.")
    else:
        print("Deletion cancelled")


while True:
    show_menu()
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        add_note()
    elif choice == 2:
        view_all_note()
    elif choice == 3:
        delete_notes()
    elif choice == 4:
        print("Exiting Note-Taiking app...Good Bye guyszzz")
        break
    else:
        print("invalid choice! try (1-4): ")
"""