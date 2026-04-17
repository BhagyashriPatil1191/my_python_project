# Tuples are used to store multiple items in a single variable. (ropund brackets)
# A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:5])
print(thistuple[2:5])

"""
Inside the editor, complete the following steps:
Create a tuple called fruits with the values "apple", "banana", "cherry"
Print the second item in the tuple
Print the number of items using len()
Unpack the tuple into three variables a, b, c
Print the variable b
"""

fruits = ("apple","bannan","cherry")
print(f"fruits {fruits[2]}")
i = 0
print(len(fruits))
(a,b,c) = fruits #unpacking tuple

print(b)
