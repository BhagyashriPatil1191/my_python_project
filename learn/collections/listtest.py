""" collections
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
thislist = ["Hello","Hi","Whatsup"]
print(thislist)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

mixList = ["1","bannana", True]

list4 = list(("yes","no"))
print(list4)

print(f"0 is {list4[0]}")
print(f"1 is {list4[1]}")
print(f"-1 is {list4[-1]}")
print(f"-2 is {list4[-2]}")

thislist = ["apple", "banana", "cherry"]
tropical = ["cherry", "cherry", "papaya"]
thislist.extend(tropical)
print(thislist)

print(thislist.sort())

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

"""
Inside the editor, complete the following steps:
Create a list called colors with the values "red", "green", "blue"
Print the first item in the list
Change the second item to "yellow"
Add "purple" to the end of the list using append()
Remove "red" from the list using remove()
Print the list
"""

colors = ["red","green","blue"]
print(colors[0])
colors[1] = "yellow"
colors.append("purple")
colors.remove("red")

print(colors)