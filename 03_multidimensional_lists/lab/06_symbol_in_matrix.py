rows = columns = int(input())

matrix = [list(input()) for _ in range(rows)]
searched_symbol = input()
coordinates = None

for row_index in range(rows):
    if coordinates:
        break
    for col_index in range(rows):
        if matrix[row_index][col_index] == searched_symbol:
            coordinates = (row_index, col_index)
            print(coordinates)
            break

if coordinates is None:
    print(f'{searched_symbol} does not occur in the matrix')
