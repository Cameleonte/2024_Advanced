def creating_sets(num):
    set_numbers = set()
    for _ in range(num):
        set_numbers.add(input())
    return set_numbers


n, m = input().split()
first_set = creating_sets(int(n))
second_set = creating_sets(int(m))

print(*first_set & second_set, sep='\n')
