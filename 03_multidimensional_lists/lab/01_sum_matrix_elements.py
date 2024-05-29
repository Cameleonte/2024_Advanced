rows, columns = [int(x) for x in input().split(', ')]

tot_sum = 0
matrix = []
for row in range(rows):
    row_data = [int(a) for a in input().split(', ')]
    tot_sum += sum(row_data)
    matrix.append(row_data)

print(tot_sum)
print(matrix)
