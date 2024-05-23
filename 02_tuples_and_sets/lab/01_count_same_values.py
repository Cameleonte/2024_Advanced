# user_data = tuple(map(float, input().split()))
#
# dict_numbers = {}
#
# for num in user_data:
#     if num not in dict_numbers.keys():
#         dict_numbers[num] = 0
#     dict_numbers[num] += 1
#
# for key, value in dict_numbers.items():
#     print(f'{key} - {value} times')

numbers = tuple([float(x) for x in input().split()])

dict_numbers = {}

for num in numbers:
    if num in dict_numbers:
        dict_numbers[num] = numbers.count(num)

for key, value in dict_numbers.items():
    print(f'{key} - {value} times')
