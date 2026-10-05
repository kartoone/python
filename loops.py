# Loops in Python examples

choice = "1"
while choice == "1":
    # display a menu
    print("1. Enter numbers")
    print("2. Quit")
    choice = input("Choice? ")

    if choice == "1":
        A=int(input("Number: "))
        B=int(input("Number: "))
        print("The max number is: ", max(A,B))
    else:
        print("Goodbye!")