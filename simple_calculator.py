def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Basic Calculator")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    while True:
        operation = input("Choose an operation (1/2/3/4/5): ")

        if operation == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if operation in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if operation == '1':
                print(f"The result is: {add(num1, num2)}")
            elif operation == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif operation == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif operation == '4':
                result = divide(num1, num2)
                print(f"The result is: {result}")
        else:
            print("Invalid operation. Please choose a valid option.")

        print("\n---")

if __name__ == "__main__":
    main()