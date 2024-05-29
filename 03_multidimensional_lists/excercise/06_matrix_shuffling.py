def check_input(mat, data, row, col):
    text = data[0]
    if text == 'swap' and len(data) == 5:
        index1, index2, index3, index4 = [int(x) for x in data[1:]]
        if 0 <= index1 <= row and 0 <= index2 <= row and 0 <= index3 <= col and 0 <= index4 <= col:
            mat[index1][index2], mat[index3][index4] = mat[index3][index4], mat[index1][index2]
            return mat
    else:
        return False


rows, cols = [int(a) for a in input().split()]

matrix = [[a for a in input().split()] for _ in range(rows)]

command = input().split()
while command[0] != 'END':
    result_check = check_input(matrix, command, rows, cols)
    if result_check:
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')
    command = input().split()
