"""
Sets are used to store multiple items in a single variable. 
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
"""

thisset = {"apple","grapes","cherry"}
print(thisset)

mixset = {"1","apple",True,"banana"}
thisnewset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

list = ["hello"]
thisnewset.update(list) #update can be done using any other collections
print(thisnewset)

#join multiple sets 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#frozensets - immutable sets
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


