commands_number = int(input())

cars_in = set()
cars_out = set()

for _ in range(commands_number):
    data = input().split(', ')
    direction, car_number = data[0], data[1]
    if direction == 'IN':
        cars_in.add(car_number)
    else:
        if car_number in cars_in:
            cars_out.add(car_number)
            cars_in.remove(car_number)

print('Parking Lot is Empty') if not cars_in else print(*cars_in, sep='\n')
