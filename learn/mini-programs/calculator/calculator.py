print("=========Simple Calculator============")
num1 = float(input("Enter first number:  "))
num2 = float(input("Enter second number:  "))

print("Choose an operation")

print("1. +")
print("2. -")
print("3. *")
print("4. /")

choice = input("Enter operator (+,-,*,/)")

if choice == "+":
    result = num1+num2
elif choice == "-":
    result = num1-num2
elif choice == "*":
    result = num1*num2
elif choice == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero."
else: 
    result = "Invalid input"
print("\nResult:", result)





