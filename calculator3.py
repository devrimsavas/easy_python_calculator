#easier calculator using dictionary. you can add any operator in dictionary.
def calculate(num1, num2, operator):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Error: it is 0 Error"
    }

    try:
        result = operations[operator](int(num1), int(num2))
        if isinstance(result, str):  # to handle division by zero error
            print(result)
            return None
        return result
    except KeyError:
        print(f"Invalid operator. Please use a valid operator: {list(operations.keys())}")
        return None

go_program = True

while go_program:
    try:
        # number 1 and number two same time with comma 
        enter_numbers = input("Enter two numbers separated by a comma, 0,0 for exit:")
        no1, no2 = enter_numbers.split(",")  # so you can enter 2 numbers in same line
    except ValueError:
        print("Please enter two numbers separated by a comma.")
        continue

    if no1.strip() == "0" and no2.strip() == "0":
        break

    if all(n.strip() == "" for n in (no1, no2)):
        print("Please enter two numbers")
        continue

    operator = input("Enter operator: ")

    result = calculate(no1, no2, operator)

    if result is not None:
        print(f'{no1.strip()} {operator} {no2.strip()} = {result}')
