rows, columns = [int(a) for a in input().split()]

matrix = [[chr(r + 97) + chr(r + c + 97) + chr(r + 97) for c in range(columns)] for r in range(rows)]

[print(*row) for row in matrix]
