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

message = input("> ")
words = message.split(' ')
print(words)
emojis = {                          # Windos key + .
    ":)":"😁",
    ":(":"😔"
}
output = ''
for word in words:
    output += emojis.get(word,word) + " "
print(output)