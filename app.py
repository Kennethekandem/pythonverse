print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("--------------------")

# -------------------

character_name = "john"
age = 35
active = False
counted_string = 'random string'
squares = [1,4,9,16]

if active:
    print(f"my name is {character_name} and i am {age} years old")
else:
    print(f"unable to get that info\nplease, try again")



print(len(counted_string))
print(counted_string[3])
print(squares)
print(squares[2])
print(squares[-1])

print(f"hello, how old are you?")
inputted = int(input())


lucky_numbers = [4, 8, 15, 16, 24]
friends = ["karen", "lucky", "max", "jon"]
friends.extend(lucky_numbers)

print(f"you are {inputted} years old")
print(friends)

#----------------------
# tuples

coordinates = (4,2)
print(coordinates)


def sayhi(value):
    if(value <= 25):
        print(f"hello, you are {value} years old? are you sure?")
    else: 
        print(f"man you are old. you mean you are {value} years old! 😳")

sayhi(inputted)

print("-------------------------")

def cube(num):
    return num*num*num

print(cube(3))


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num2:
        return num2
    else:
        return num3
    
print(max_num(10, 40, 5))


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



print("---------------- dictionary")

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Love", "Not a valid key!"))

i = 1

while i <= 20:
    print(i)
    i+=1

print("done with the loop")


print("---------game time!")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess:")
        guess_count += 1
    else: 
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses -- lost!")
else:
    print("you win!")