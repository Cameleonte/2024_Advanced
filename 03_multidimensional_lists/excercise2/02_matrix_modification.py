def operations(data, mat):
    action = data[0]
    row, col, value = [int(a) for a in data[1:]]
    if 0 <= row <= len(mat) - 1 and 0 <= col <= len(mat) - 1:
        if action == 'Add':
            mat[row][col] += value
        elif action == 'Subtract':
            mat[row][col] -= value
        return mat
    else:
        return False


rows = cols = int(input())

matrix = [[int(a) for a in input().split()] for _ in range(rows)]

command = input().split()
while command[0] != 'END':
    result = operations(command, matrix)
    if not result:
        print(f'Invalid coordinates')
    command = input().split()

[print(*row) for row in matrix]
