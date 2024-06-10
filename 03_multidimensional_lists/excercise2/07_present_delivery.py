ROWS = COLS = int(input())
MOVEMENTS = {'up': (- 1, 0), 'down': (1, 0), 'left': (0, - 1), 'right': (0, 1)}


def check_limits(board, old_man, gifts, direction):
    row = old_man[0] + MOVEMENTS[direction[1]][0]
    col = old_man[1] + MOVEMENTS[direction[1]][1]
    if 0 <= row < ROWS and 0 <= col < COLS:
        if matrix[row][col] == 'V':
            gifts -= 1
            matrix[row][col] = '-'
        elif matrix[row][col] == 'X':
            matrix[row][col] = '-'
        elif matrix[row][col] == 'C':
            pass


presents = int(input())
matrix = []
naughty_kids = []
nice_kids = []
santa = []
cookies = []

for row_ind in range(ROWS - 1):
    line = input().split()
    matrix.append(line)
    for col_ind in range(COLS - 1):
        if line[col_ind] == 'S':
            santa = [row_ind, col_ind]
        elif matrix[row_ind][col_ind] == 'X':
            naughty_kids.append([row_ind, col_ind])
        elif matrix[row_ind][col_ind] == 'V':
            nice_kids.append([row_ind, col_ind])
        elif matrix[row_ind][col_ind] == 'C':
            cookies.append([row_ind, col_ind])

command = input()
while True:
    if presents <= 0 or len(command) > 5:
        break
