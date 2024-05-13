from collections import deque

water_qty = int(input())

name = input()
queue = deque()

while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    list_command = command.split()
    if len(list_command) == 1:
        remove_person = queue.popleft()
        if int(command) <= water_qty:
            water_qty -= int(command)
            print(f'{remove_person} got water')
        else:
            print(f'{remove_person} must wait')
    else:
        liters_to_add = int(list_command[1])
        water_qty += liters_to_add

    command = input()

print(f'{water_qty} liters left')
