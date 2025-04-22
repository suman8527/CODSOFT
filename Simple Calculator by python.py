# Simple calculator using if-else

print("Calculator Program")
print("Enter two numbers")

a = float(input("First number: "))
b = float(input("Second number: "))

print("Choose operation:")
print(" + for addition")
print(" - for subtraction")
print(" * for multiplication")
print(" / for division")

op = input("Enter operation: ")

if op == '+':
    result = a + b
    print("Addition is", result)

elif op == '-':
    result = a - b
    print("Subtraction is", result)

elif op == '*':
    result = a * b
    print("Multiplication is", result)

elif op == '/':
    if b != 0:
        result = a / b
        print("Division is", result)
    else:
        print("Cannot divide by 0")

else:
    print("Invalid operator entered")
