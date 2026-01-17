def divide(number):
    # Convert input to a numeric type (float) to allow division
    try:
        numeric = float(number)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid input for division: {number}")
    return 100 / numeric


if __name__ == "__main__":
    while True:
        inpt = input("enter a number: ")
        
        print(divide(inpt))
