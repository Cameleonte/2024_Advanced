rows, columns = [int(a) for a in input().split(', ')]

matrix = [[int(a) for a in input().split()] for _ in range(rows)]
for column in range(columns):
    column_sum = 0
    for row in range(rows):
        column_sum += matrix[row][column]
    print(column_sum)
