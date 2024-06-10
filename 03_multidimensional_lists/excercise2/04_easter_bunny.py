rows = cols = int(input())

matrix = []
b_position = []

for row_index in range(rows):
    current_row = input().split()
    matrix.append(current_row)
    if "B" in current_row:
        col_b_index = current_row.index('B')
        b_position.extend([row_index, col_b_index])

possible_moves = {'right': [0, 1], 'left': [0, - 1], 'up': [- 1, 0], 'down': [1, 0]}
max_eggs = - float('inf')
direction = ''
max_matrix = []

for current_direction, move in possible_moves.items():
    b_row = b_position[0] + move[0]
    b_col = b_position[1] + move[1]
    current_eggs = 0
    current_egg_matrix = []

    while 0 <= b_row < rows and 0 <= b_col < cols:
        if matrix[b_row][b_col] == "X":
            break
        current_eggs += int(matrix[b_row][b_col])
        current_egg_matrix.append([b_row, b_col])
        b_row += move[0]
        b_col += move[1]

    if current_eggs > max_eggs and current_egg_matrix:
        max_eggs = current_eggs
        max_matrix = current_egg_matrix
        direction = current_direction

print(direction)
[print(row) for row in max_matrix]
print(max_eggs)
