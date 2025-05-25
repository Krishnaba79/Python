first = int(input("Enter Your First Number: "))
operator = input("Enter Your Operator (+, -, *, %, /): ")
second = int(input("Enter Your Second Number: "))

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "%":
    print(first % second)
elif operator == "/":
    print(first / second)
else:
    print("Invalid Input")
