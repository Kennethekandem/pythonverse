print("------------------------------- calculator")

value_one = float(input("Input first number: "))
operator = input("add operator: ")
value_two = float(input("Input the second number: "))

supported_operators = ["+", "-", "*", "/"]

def check_operator(operator):
    if operator not in supported_operators:
        print("invalid operator")
    else:
        return True

def calculate(value_one, value_two, operator):
    # confirm_operator = check_operator(operator)
    
    if not check_operator(operator):
        return None
    if operator == supported_operators[0]:
        print(value_one + value_two)
    elif operator == supported_operators[1]:
        print(value_one - value_two)
    elif operator == supported_operators[2]:
        print( value_one * value_two)
    elif operator == supported_operators[3]:
        print(value_one / value_two)
    

    
calculate(value_one, value_two, operator)