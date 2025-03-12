num1 = float(input("10:"))
num2 = float(input("5:"))
#This will ask the user to input two numbers
#propmt the user to input two numbers
result =int(input("Enter numbers (0-9): "))
if operation == '+'
result = num1+num2
print(f"{num1}+{num2} = {result}")
elif operation =='*':
result = num1*num2
print(f"{num1}*{num2}={result}")
elif operatiom == '-'
result = num1-num2
print(f"{num1}-{num2}={result}")
elif operation  == '/':
if num2 == 0:
    print("error:division by zero is not allowed.")
else:
    result = num1/num2
    print(f"{num1}/{num2}={result}")
else:
print("Invalid operation.Please enter +,-,/, or *.")
except ValueError:
print("Invalid Input.Please enter numbers only.")

if _ _ name _ _ =="main_ _:"
basic calculator()