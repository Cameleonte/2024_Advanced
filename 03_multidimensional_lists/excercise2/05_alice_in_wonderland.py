rows = cols = int(input())

matrix = []
alice = []
for row_ind in range(rows):
    matrix.append(input().split())
    if not alice:
        for col_ind in range(cols):
            if matrix[row_ind][col_ind] == "A":
                alice = [row_ind, col_ind]
                break

possible_moves = {'up': [- 1, 0], 'down': [1, 0], 'left': [0, - 1], 'right': [0, 1]}
tea = 0
ready = False

while True:
    next_move = possible_moves[input()]
    matrix[alice[0]][alice[1]] = '*'
    curr_r_ind = next_move[0] + alice[0]
    curr_c_ind = next_move[1] + alice[1]
    if 0 <= curr_r_ind < rows and 0 <= curr_c_ind < cols:
        if matrix[curr_r_ind][curr_c_ind] == 'R':
            matrix[curr_r_ind][curr_c_ind] = '*'
            break
        alice = [curr_r_ind, curr_c_ind]
        curr_position = matrix[curr_r_ind][curr_c_ind]
        if curr_position.isdecimal():
            tea += int(matrix[curr_r_ind][curr_c_ind])
            matrix[curr_r_ind][curr_c_ind] = 'A'
            if tea >= 10:
                matrix[curr_r_ind][curr_c_ind] = '*'
                ready = True
                break
        elif curr_position == '*':
            continue
        else:
            matrix[curr_r_ind][curr_c_ind] = 'A'
            if tea >= 10:
                ready = True
                break
    else:
        if ready:
            matrix[curr_r_ind][curr_c_ind] = '*'
        break

if ready:
    print('She did it! She went to the party.')
    [print(*row) for row in matrix]
else:
    print("Alice didn't make it to the tea party.")
    [print(*row) for row in matrix]
