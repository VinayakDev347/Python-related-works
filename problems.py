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

#21) Safe Calculator 
"""
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        raise ZeroDivisionError ("cannot divide by Zero")
    return x / y

def menu():
    print("\n-----Safe Calculator------")
    print("1. Addition")
    print("2. Substract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    menu()
    choice = int(input("Enter your valid choice (1-5) : "))
    if choice == 5:
        print("Exiting Calculator. Bye")
        break
    try:
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))

        if choice == 1:
            print("Result is :", add(num1,num2))
        elif choice == 2:
            print("Result is :",sub(num1,num2))
        elif choice == 3:
            print("Result is :",mul(num1,num2))
        elif choice == 4:
            print("Result is :",div(num1,num2))
        else:
            print("Invalid choice...Select any valid option")

    except ValueError:
            print("Invalid input.Enter Valid Number")
    except ZeroDivisionError as e:
        print("Error: ",e)
    except Exception as e:
        print(f"An Unexcepected error occured:{e}")
    finally:
        print("Thankyou for using safe calculator.")
"""

#22) Temperature Convertor
"""
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
      return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
      return (fahrenheit - 32 ) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
      return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
      return (kelvin - 273.15)

def menu():
    print("\n-----Temperature Converter Menu-----")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter Your choice (1/2/3/4) : ")

    if choice == '1':
        celsius = float(input("Enter the temperature in  Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(celsius): .2f}")
        print(f"Kelvin: {celsius_to_kelvin(celsius): .2f}")
    elif choice == '2':
        fahrenheit = float(input("Enter the Temperature in Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celsius(fahrenheit): .2f}")
        print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit): .2f}")
    elif choice == '3':
        kelvin = float(input("Enter the temperature in Kelvin: "))
        print(f"Celsius: {kelvin_to_celsius(kelvin): .2f}")
        print(f"Fahrenheit: {celsius_to_kelvin(kelvin): .2f}")
    elif choice == '4':
        print("Exiting from the calculator")
        break
    else:
        print("invalid choice!!!")
"""

#23) Student Grade Management  
"""
student_score = input("Enter the students score seperated with comas ")
scores =[int(score) for score in student_score.split(",")]

grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
    for score in scores
]

passing_student = [score for score in scores if score >= 60]
failing_student = [score for score in scores if score < 60]

print("\n-----Student Grade-----\n")
for i,(score,grade) in enumerate(zip(scores,grades),start=1):
    print(f"Student {i}: Score = {score},Grade = {grade}")

print("Student score: ",scores)
print("Grades: ",grades)

print("\n-----Passing and Failing Student-----\n")
print("Passing Student: ",passing_student)
print("Failing Student: ",failing_student)
"""

#24) Random Password Generator
"""
import random, string

def generate_pass(length = 12):
    if length < 4:
        raise ValueError("Password length must be at least 4 charactor")
    
    uppercase = string.ascii_uppercase
    lowercase =string.ascii_uppercase
    digits = string.digits
    specal_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(specal_chars),
    ]

    all_char = uppercase + lowercase + digits + specal_chars
    password += random.choices(all_char,k=length - 4)

    random.shuffle(password)
    return ''.join(password)

try:
    length = int(input("Enter the desired Password length (minimum 4): "))
    password = generate_pass(length)
    print('Generated Password:',password)
except ValueError as e:
    print(e)
"""
#25) Recipe Viewer App
"""
#loading recipe from file path 
def load_recipe(file_path):
    try:
        with open(file_path,"r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipe_dict = {}
            for recipe in recipes:
                lines = recipe.split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace('ingredients: ','').strip()
                    instructions = lines[2].replace('instructions: ','').strip()
                    recipe_dict[name] = {"ingredients":ingredients, "instructions": instructions}
            return recipe_dict
    except FileNotFoundError:
        print("File not Found!!!")
        return()
#Display recipe Menu
def show_menu():
    print("-----Recipe Viewer Menu-----")
    print("1. View Recipe by Name")
    print("2. List all the Recipes")
    print("3. Exit ")

def view_recipe(recipes):
    name = input("Enter the name of the recipe: ")
    if name in recipes:
        print(f"\n-----Recipe {name} Details-----")
        print(f"Name: {name}")
        print(f"Ingredients: {recipes[name]['ingredients']}")
        print(f"Instructions: {recipes[name]['instructions']}")
    else:
        print("Recipe Not Found")

recipe_file = "recipe.txt"
recipes = load_recipe(recipe_file)

while True:
    show_menu()
    choice = input("Enter Your choice (1/2/3): ")

    if choice == '1':
        view_recipe(recipes)
    elif choice == '2':
        print("-----All Recipes-----")
        for name in recipes:
            print(name)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice,please try again...")
"""

#26) Daily Journal Logger
'''
journal_file = 'daily_journal.txt'

def add_entry():
    entry = input("Write your Journal entry: ")
    with open(journal_file,'a') as file:
        file.write(entry + '\n')
    print("Entry Added Successfully!")

def view_entry():
    try:
        with open(journal_file,'r') as file:
            content = file.read()
            if content:
                print("\n-----Your Journal Entries-----")
                print(content)
            else:
                print("No entries found. Start writing Today Itself")
    except FileNotFoundError:
        print("No Journal file Found. Add an entry first!")

def search_entry():
    keyword = input("Enter a keyword to search: ").lower()
    try:
        with open(journal_file,'r') as file:
            content = file.readlines()
            found = False
            print("\n-----Search List-----")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
                if not found:
                    print("No matching results found")
    except FileNotFoundError:
        print("No Journal file found, Add an entry first!")

def show_menu():
    print("\n-----Daily Journal Menu")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search entries by keyword")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter Your choice(1-4): ")
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entry()
    elif choice == '3':
        search_entry()
    elif choice == '4':
        print("Exited!!!")
        break
    else:
        print("invalid choice ,please enter a number between 1 and 4")
'''
#27) Student Report Generator
"""
import csv

def process_student_data(input_file,output_file):
    try:
        with open(input_file,'r') as infile:
            reader = csv.DictReader(infile)
            student_reports = []
            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                average = round((math+science+english) / 3,2)
                status = "Pass" if average >= 60 else "Fail"

                student_reports.append({
                    'Name' : name,
                    'Math' : math,
                    'Science' : science,
                    'English' : english,
                    'Average' : average,
                    'Status' : status
                })
        with open(output_file,'w',newline='') as outfile:
            fieldnames = ['Name','Math','Science','English','Average','Status']
            writer = csv.DictWriter(outfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)
        
        print(f"Students Report generated in {output_file}successfully...")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except KeyError:
        print(f"Error: Invalid coloumn names in the input file")
    except Exception as e:
        print(f"An a error occured: {e}")

input_file = 'students.csv'
output_file = 'students_report.csv'
process_student_data(input_file,output_file)
"""
#28) Mini To do App
"""
import json
import os

TASK_FILE = 'my_tasks.json'

if not os.path.exists(TASK_FILE):
  with open(TASK_FILE, 'w') as file:
    json.dump([], file)

def load_tasks():
  with open(TASK_FILE, 'r') as file:
    return json.load(file)

def save_tasks(tasks):
  with open(TASK_FILE, 'w') as file:
    json.dump(tasks, file, indent=2)

def add_task():
  task_name = input("Enter the task name: ").strip()
  tasks = load_tasks()
  tasks.append({"task": task_name, "status": "Incomplete"})
  save_tasks(tasks)
  print(f'Task "{task_name}" added successfully!')

def view_tasks():
  tasks = load_tasks()
  if tasks:
    print("\n--- To-Do List ---")
    for idx, task in enumerate(tasks, start=1):
      print(f"{idx}. {task['task']} - {task['status']}")
  else:
    print("No tasks found.")

def update_status():
  tasks = load_tasks()
  view_tasks()
  try:
    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
      new_status = input("Enter the new status (Complete/Incomplete): ").strip()
      tasks[task_index]['status'] = new_status
      save_tasks(tasks)
      print("Task status updated successfully!")
    else:
      print("Invalid task number.")
  except ValueError:
    print("Invalid input. Please enter a valid task number.")

# Step 6: Delete a Task
def delete_task():
  tasks = load_tasks()
  view_tasks()
  try:
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
      deleted_task = tasks.pop(task_index)
      save_tasks(tasks)
      print(f'Task "{deleted_task["task"]}" deleted successfully!')
    else:
      print("Invalid task number.")
  except ValueError:
    print("Invalid input. Please enter a valid task number.")

def display_menu():
  print("\n--- Mini To-Do App ---")
  print("1. Add a new task")
  print("2. View all tasks")
  print("3. Update Task status")
  print("4. Delete a task")
  print("5. Exit")

while True:
  display_menu()
  choice = input("Enter your choice (1-5): ").strip()

  if choice == '1':
    add_task()
  elif choice == '2':
    view_tasks()
  elif choice == '3':
    update_status()
  elif choice == '4':
    delete_task()
  elif choice == '5':
    print("Exiting the To-Do List App. Goodbye!")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 5.")
"""
#29) Weather App using OpenWeather API
"""
import requests

API_KEY = "597a205a674c26be42eb8fe94123369e"

city = 'Kannur'
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"


def getWeather_city(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City" : data['name'],
                "Temperature" : f"{data['main']['temp']}C",
                "Weather" : data["weather"][0]['description'].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed":f"{data['wind']['speed']}m/s"
                }
            return weather
        elif response.status_code == 404:
            print("City not found")
        else:
            print("An error occured. Status Code: ",response.status_code)
    except Exception as e:
        print("An Error occured: ",e)
    return None

def display_weather(weather):
    print("\n-----Weather Information-----")
    for key,value in weather.items():
        print(f"{key}: {value}")

while True:
    print("\n-----Weather App-----")
    city = input("Enter Your city name ( or 'q' to Quit) : ").strip()
    if city.lower() == 'q':
        break
    weather = getWeather_city(city)
    if weather:
        display_weather(weather)
"""