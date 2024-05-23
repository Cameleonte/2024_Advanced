lines_count = int(input())

elements_set = set()

for line in range(1, lines_count + 1):
    list_elements = input().split()
    for element in list_elements:
        elements_set.add(element)

print(*elements_set, sep='\n')
