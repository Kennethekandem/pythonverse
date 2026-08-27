print("--------------Read file")

employee_file = open("employees.txt", "r")

# print(employee_file.readable())

if employee_file.readable():
    print(True)
else:
    print('not readable')

for employee in employee_file.readlines():
    print(employee + "filessssss")

employee_file.close()

employee_file = open("employees.txt", 'a')

if employee_file.readable():
    print(True)
else:
    print("not readable")

employee_file.write("Toby", "Carpenter")
employee_file.close()