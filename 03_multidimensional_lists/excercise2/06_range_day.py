ROW = COL = 5

matrix = []
my_position = []
targets = 0
targets_down = []

for row in range(ROW):
    matrix.append(input().split())
    for col in range(COL):
        if matrix[row][col] == 'A':
            my_position = [row, col]
        if matrix[row][col] == 'x':
            targets += 1

directions = {'up': (- 1, 0), 'down': (1, 0), 'left': (0, - 1), 'right': (0, 1)}

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'shoot':
        row = my_position[0] + directions[command[1]][0]
        col = my_position[1] + directions[command[1]][1]
        while 0 <= row < ROW and 0 <= col < COL:
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                targets -= 1
                targets_down.append([row, col])
                break
            row += directions[command[1]][0]
            col += directions[command[1]][1]
        if targets == 0:
            print(f'Training completed! All {len(targets_down)} targets hit.')
            break
    elif command[0] == 'move':
        row = my_position[0] + directions[command[1]][0] * int(command[2])
        col = my_position[1] + directions[command[1]][1] * int(command[2])
        if 0 <= row < ROW and 0 <= col < COL and matrix[row][col] == '.':
            matrix[row][col] = 'A'
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [row, col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in targets_down]
