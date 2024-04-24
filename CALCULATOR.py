def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y

def main():
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("Choose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        print("Result:", result)

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != "yes":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
