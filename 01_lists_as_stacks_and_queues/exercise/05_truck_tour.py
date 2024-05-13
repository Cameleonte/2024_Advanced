from collections import deque


def check_fuel(my_deque, counter=0, success=False):
    current_tot_fuel = 0
    current_tot_km = 0
    for pump in range(len(my_deque)):
        current_tot_fuel += my_deque[pump][0]
        current_tot_km += my_deque[pump][1]
        if pump == len(my_deque) - 1:
            return counter
        if current_tot_fuel < current_tot_km:
            my_deque.rotate(-1)
            counter += 1
            return check_fuel(my_deque, counter, success)

        elif current_tot_fuel >= current_tot_km and pump == len(my_deque) - 1:
            success = True
    return success


pumps_count = int(input())
tot_stations_deque = deque()

for index in range(pumps_count):
    current_pump = list(map(int, input().split()))
    tot_stations_deque.append(current_pump)

pump_index = check_fuel(tot_stations_deque)
print(pump_index)
