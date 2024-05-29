rows = int(input())

matrix = [[int(a) for a in input().split(', ') if int(a) % 2 == 0] for row in range(rows)]

print(matrix)
