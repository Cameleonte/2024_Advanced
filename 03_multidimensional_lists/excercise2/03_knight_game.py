rows = cols = int(input())

matrix = []
knights = []

for row in range(rows):
    matrix.append([cols for cols in input()])
    for col in range(cols):
        if matrix[row][col] == 'K':
            knights.append([row, col])

removed_knights = 0
possible_moves = [(1, 2), (1, - 2), (- 1, 2), (- 1, - 2), (2, 1), (2, - 1), (- 2, 1), (- 2, - 1)]

while True:
    max_hits = 0
    max_knight = [0, 0]
    for row_ind, col_ind in knights:
        current_hits = 0
        for move in possible_moves:
            next_r_pos = row_ind + move[0]
            next_c_pos = col_ind + move[1]
            if 0 <= next_r_pos < rows and 0 <= next_c_pos < rows:
                if matrix[next_r_pos][next_c_pos] == 'K':
                    current_hits += 1
        if current_hits > max_hits:
            max_hits = current_hits
            max_knight = [row_ind, col_ind]
    if max_hits == 0:
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)
