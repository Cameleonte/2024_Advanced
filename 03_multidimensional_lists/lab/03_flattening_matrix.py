rows = int(input())

# flatten_m = []
# for _ in range(rows):
#     for num in input().split(', '):
#         flatten_m.append(int(num))
#
# print(flatten_m)

matrix = [[int(a) for a in input().split(', ')] for _ in range(rows)]

flatten_matrix = [num for row in matrix for num in row]

print(flatten_matrix)
