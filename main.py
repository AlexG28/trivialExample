def divide(number): 
    return 100 / number


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <number>")
        sys.exit(1)
    try:
        num = float(sys.argv[1])
    except ValueError:
        print("Invalid number provided.")
        sys.exit(1)
    try:
        result = divide(num)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        sys.exit(1)
    print(result)

