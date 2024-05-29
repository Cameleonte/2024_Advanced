rows = cols = int(input())

matrix = [[int(a) for a in input().split()] for _ in range(rows)]

# primari_d_sum = 0
# secondary_d_sum = 0
#
# for row_index in range(rows):
#     for col_index in range(cols):
#         if row_index == col_index:
#             primari_d_sum += matrix[row_index][col_index]
#
# for row_index in range(rows):
#     for col_index in range(cols, -1, -1):
#         if row_index + col_index == rows - 1:
#             secondary_d_sum += matrix[row_index][col_index]
#
# print(abs(primari_d_sum - secondary_d_sum))

primari_diagonal = [matrix[a][a] for a in range(rows)]
secondary_diagonal = [matrix[a][-1 - a] for a in range(rows)]
difference = abs(sum(primari_diagonal) - sum(secondary_diagonal))
print(difference)
