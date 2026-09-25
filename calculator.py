num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
print("1 for +, 2 for -, 3 for *, 4 for /")
op = input()
if op == "1":
    answer = num1 + num2
elif op == "2":
    answer = num1 - num2
elif op == "3":
    answer = num1 * num2
elif op == "4":
    answer = num1 / num2
else:
    answer = "Invalid choice"
print(answer)


