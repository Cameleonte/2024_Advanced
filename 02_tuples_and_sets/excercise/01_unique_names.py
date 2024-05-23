names_number = int(input())

set_names = set()

for _ in range(names_number):
    name = input()
    set_names.add(name)

print(*set_names, sep='\n')
