rows = columns = int(input())

matrix = [[int(a) for a in input().split()] for _ in range(rows)]

tot_sum = 0
for row in range(rows):
    for col in range(columns):
        if row == col:
            tot_sum += matrix[row][col]

print(tot_sum)

# for index in range(rows):
#     tot_sum += matrix[index][index]
#
# print(tot_sum)