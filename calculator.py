# Junior+ Level Calculator
# Supports:
# - operation loop
# - multiple operations
# - calculation history
# - error handling

history = []

print("=== Smart Calculator ===")

while True:
    print("\nAvailable operations:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("** Exponentiation")
    print("%  Modulo")
    print("history - Show History")
    print("exit    - Quit")

    operation = input("\nEnter operation: ")

    # Exit the program
    if operation == "exit":
        print("Exiting calculator...")
        break

    # Show history
    if operation == "history":
        print("\n=== Calculation History ===")

        if len(history) == 0:
            print("History is empty")
        else:
            for item in history:
                print(item)

        continue

    # Validate operation
    allowed_operations = ["+", "-", "*", "/", "**", "%"]

    if operation not in allowed_operations:
        print("Error: unknown operation")
        continue

    # Input numbers with error handling
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Error: please enter numbers only!")
        continue

    # Perform operations
    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num2 == 0:
            print("Error: division by zero!")
            continue

        result = num1 / num2

    elif operation == "**":
        result = num1 ** num2

    elif operation == "%":
        result = num1 % num2

    # Format result string
    answer = f"{num1} {operation} {num2} = {result}"

    print("Result:", result)

    # Save to history
    history.append(answer)
