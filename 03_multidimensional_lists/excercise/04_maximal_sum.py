rows, cols = [int(a) for a in input().split()]

matrix = [[a for a in input().split()] for _ in range(rows)]

max_sum = -float('inf')
max_row_index = 0
max_col_index = 0

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_sum = 0
        for a in range(row_index, row_index + 3):
            for b in range(col_index, col_index + 3):
                current_sum += int(matrix[a][b])
        if current_sum > max_sum:
            max_sum = current_sum
            max_row_index = row_index
            max_col_index = col_index

print(f'Sum = {max_sum}')

max_smatrix = [matrix[r_index][max_col_index:max_col_index + 3] for r_index in range(max_row_index, max_row_index + 3)]

[print(*row) for row in max_smatrix]
