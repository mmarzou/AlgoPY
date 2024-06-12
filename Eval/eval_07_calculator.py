print ("Calculator Program")
# Check if the input is a number, if not, ask again for a number.
while True:
    try:
        result = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

# Check if the input is a valid operation, if not, ask again for an operation.
while True:
    operation = str(input("Sasir une opéation (+ - * /) ou stop: "))
    while operation not in ['+', '-', '*', '/', 'stop', 's', 'quit']:
        print("Invalid operation")
        operation = str(input("Sasir une opéation (+ - * /) ou stop: "))
    if operation == 'stop' or operation == 's' or operation == 'quit':
        break
    # Check if the input is a number, if not, ask again for a number.
    while True:
        try:
            nbrInput2 = float(input("Enter another number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    if operation == "+":
        result += nbrInput2
    elif operation == "-":
        result -= nbrInput2
    elif operation == "*":
        result *= nbrInput2
    elif operation == "/":
        result /= nbrInput2
    print(result)
print("Program stopped")