#Basic calculator program

#Get user input
num1 =float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#perform calculation based on the operation
if operation == '+':
   result = num1 + num2
   print(f"{num1} + {num2} = {result}")
elif operation =='*':
     result = num1 * num2
     print(f"{num1} * {num2}={result}")
elif operatiom == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation  == '/':
    if num2 != 0:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
 else:
    print("Error! Division by zero is not allowed.")   
 else:
print("Invalid operation.Please enter +,-,*, or /.")
except ValueError:
print("Invalid Input.Please enter numbers only.")

print {num1} {operation} {num2} = {result}
