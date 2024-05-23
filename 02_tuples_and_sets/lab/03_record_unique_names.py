count_names = int(input())

unique_names = set()

for _ in range(count_names):
    name = input()
    unique_names.add(name)

for n in unique_names:
    print(n)
