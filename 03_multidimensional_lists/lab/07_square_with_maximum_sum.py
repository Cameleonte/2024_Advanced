rows, columns = [int(a) for a in input().split(', ')]

matrix = [[int(s) for s in input().split(', ')] for _ in range(rows)]
max_sum_sub_matrix = float('-inf')
found_matrix = None

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_sum = 0
        first_value, second_value, third_value, fourth_value = [matrix[row_index][col_index],
                                                                matrix[row_index][col_index + 1],
                                                                matrix[row_index + 1][col_index],
                                                                matrix[row_index + 1][col_index + 1]]
        current_sum += first_value + second_value + third_value + fourth_value
        current_sub_matrix = [[first_value, second_value], [third_value, fourth_value]]
        if current_sum > max_sum_sub_matrix:
            max_sum_sub_matrix = current_sum
            found_matrix = current_sub_matrix

for row in found_matrix:
    print(*row)
print(max_sum_sub_matrix)
