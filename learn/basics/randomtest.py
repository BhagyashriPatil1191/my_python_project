#Random number
import random
print(random.randrange(1,10))

x = 5
y = 3.14
z = 2+3j
print(type(x), type(y), type(z))

#'hello' is same as "hello"

#looping thr a string
for d in "banana":
    print(d)

abc = "hello world!"
len(abc)
print(len(abc))
print("hello" in abc)

#If else 
if "hello" in abc:
    print("YES")
else:
    {print("NO")}


if "hello" not in abc:
    print("NO")
else:
    {print("YES")}


#Slicing
b = "Hello World.  "
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

a = "           Hello World"
d = 44
print(a.upper())
print(a.strip())
print(f"Hello whatsup {d}")
print(b.rstrip())

x = 5
y = 6
if x is not y:
    print("YES")
else:
    print("YES")


print(f"answer is {x % y}")
print(f"power of {x ** y }")

