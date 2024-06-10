data = [x.replace('  ', ' ').strip().split() for x in input().split('|')]

for index in range(len(data) - 1, - 1, - 1):
    if data[index]:
        print(*data[index], end=' ')
