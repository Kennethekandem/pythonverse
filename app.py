import useful_tools
from phone import Phone
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")
# print("--------------------")

# # -------------------

# character_name = "john"
# age = 35
# active = False
# counted_string = 'random string'
# squares = [1,4,9,16]

# if active:
#     print(f"my name is {character_name} and i am {age} years old")
# else:
#     print(f"unable to get that info\nplease, try again")



# print(len(counted_string))
# print(counted_string[3])
# print(squares)
# print(squares[2])
# print(squares[-1])

# print(f"hello, how old are you?")
# inputted = int(input())


# lucky_numbers = [4, 8, 15, 16, 24]
# friends = ["karen", "lucky", "max", "jon"]
# friends.extend(lucky_numbers)

# print(f"you are {inputted} years old")
# print(friends)

# #----------------------
# # tuples

# coordinates = (4,2)
# print(coordinates)


# def sayhi(value):
#     if(value <= 25):
#         print(f"hello, you are {value} years old? are you sure?")
#     else: 
#         print(f"man you are old. you mean you are {value} years old! 😳")

# sayhi(inputted)

# print("-------------------------")

# def cube(num):
#     return num*num*num

# print(cube(3))


# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num2:
#         return num2
#     else:
#         return num3
    
# print(max_num(10, 40, 5))

# print("-----------------------for loops")

# letters = ["Forbidden", "Hate", "Redemption"]

# # for letter in letters:
# #     print(letter)

# for index in range(len(letters)):
#     print(letters[index])

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for i in range(pow_num):
#         result = result * base_num
#     return result

# print(f"it is raised to -- {raise_to_power(3, 4)}")

# print("----------nested for loop & 2D grid")
# number_grid = [
#     [1, 2, 2, 4],
#     [5, 6, 7, 8],
#     [9, 9, 9],
#     [0]
# ]

# print(number_grid[0][2])

# for row in number_grid:
#     for col in row:
#         print(col)





# print("--------- try/catch")

# try:
#     print(int(input("enter a number: ")))
# except ZeroDivisionError as err: 
#     print(f"Error: {err}")
# except ValueError:
#     print("invalid input")


text = "my cat is from jamaica and the cat used wore a cap from jamaica all the time till my mum removed it. cat watching is cool"

text.lower()
words = text.split()

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)


print(useful_tools.roll_dice(int(input("add a number: "))))

iphone = Phone("iPhone 16", "li-Ion battery x3", "6x4", "active", True)
print(iphone.battery)