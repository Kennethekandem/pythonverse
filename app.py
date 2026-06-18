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