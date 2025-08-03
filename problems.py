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