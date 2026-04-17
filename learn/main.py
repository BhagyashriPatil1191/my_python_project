
#how to print
print("This is my first project in python")
print(1)
print(2+3)
print(2*4 ,"Hello")
print("Hello hello ", 17/2)

#This is my comment
print("comment test")
"""
This is multiline comment
Do not use this code
"""
print("what's up")

"""
Creating variables
"""
x=4
name = "Bhagyashri"
print(x,name)
print(type(x), type(name))

#many values to multiple values 
x,y,z = 'Hello',12, "Shri"
print(x,y,z)

""" datatypes
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

a = "Shital"
b = 5
c = 1.2
d = 1j
e = ["hello", "Hi", "test"]
f = ("hello", "Hi", "test")
g = range(8)
h = {"name" : "John", "age" : 36, "keys": "values"}
i = {"apple", "banana", "cherry"}
j = frozenset({"apple", "banana", "cherry"})
k = bool
l = b"Hello"
m = bytearray(5)
n = memoryview(bytearray(5))
o = None

print(a,"\n",
      b,"\n",
      c,"\n",
      d,"\n",
      e,"\n",
      f,"\n",
      g,"\n",
      h,"\n",
      i,"\n",
      j,"\n",
      k,"\n",
      l,"\n",
      m,"\n",
      n,"\n",
      o,"\n")