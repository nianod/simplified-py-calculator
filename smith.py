operator = input("select an operator (/ + - *): ")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if operator == "/":
    result = num1 / num2
    print((f"answer is {round(result ,3)}"))
elif operator == "+":
    result = num1 + num2
    print(f"answer is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"answer is {result}")
elif operator == "*":
    result = num1 * num2 
    print(f"answer is {result}")
else:
    print(f"{operator} is not a valid operator")


choice = input("Do you want to perform another calculation? (yas/no: )")
if choice.lower() != 'yes':
    print("Ok Goodbye!")
    






