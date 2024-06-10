from collections import deque

rows, cols = (int(a) for a in input().split())

string = deque(input())

matrix = []
for row_index in range(rows):
    sub_m = []
    for col_index in range(cols):
        symbol = string.popleft()
        if row_index % 2 == 0:
            sub_m.append(symbol)
        else:
            sub_m.insert(0, symbol)
        string.append(symbol)
    matrix.append(sub_m)
[print(*row, sep='') for row in matrix]
