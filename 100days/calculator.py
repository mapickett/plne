import art

print(art.calc)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def get_number(position):
    """Returns a valid number"""
    while True:
        num = input(f"What's the {position} number?: ")
        try:
            float(num)
            return float(num)
        except ValueError:
            print("Invalid choice")

def get_operator():
    """Returns a valid operator"""
    while True:
        for item in operations:
            print(item)
        op = input("Pick an operation: ")
        if op in operations:
            return op
        else:
            print("Invalid choice.")

if __name__ == "__main__":

    choice = "n"
    while True:
        if choice == "y":
            n1 = result
        else:
            n1 = get_number("first")
        op1 = get_operator()
        n2 = get_number("second")
        result = operations[op1](n1, n2)
        print(f'{n1} {op1} {n2} = {result}')
        choice = input(f"""
Type 'y' to continue calculating with {result} 
Type 'n' to start a new calculation
Type 'x' to exit the calculator
Enter your choice: """)
        if choice == "x":
            break