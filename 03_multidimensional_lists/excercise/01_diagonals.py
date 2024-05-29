n = int(input())

matrix = [[int(s) for s in input().split(', ')] for _ in range(n)]

diagonal1 = []
diagonal2 = []
first_sum = 0
second_sum = 0

for row in range(n):
    for col in range(n):
        if row == col:
            primary_diagonal_value = matrix[row][col]
            diagonal1.append(primary_diagonal_value)
            first_sum += primary_diagonal_value
for row in range(n):
    for col in range(n - 1, -1, -1):
        if row + col + 1 == n:
            secondary_diagonal_value = matrix[row][col]
            diagonal2.append(secondary_diagonal_value)
            second_sum += secondary_diagonal_value

print(f'Primary diagonal: {", ".join(map(str, diagonal1))}. Sum: {first_sum}\n'
      f'Secondary diagonal: {", ".join(map(str, diagonal2))}. Sum: {second_sum}')
