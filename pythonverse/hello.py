x = 5
name = 'kenneth'
print(name)
name = 'bobby'
print(name)

print('pick a number.')
first_num = input()
print('add the second number')
second_number = input()
sum = int(first_num)+int(second_number)
print(f'total: {sum}')

if sum > 10:
    print('this is greater than 10')
elif sum == 10:
    print('this equals 10')
else:
    print('this is less than 10')
