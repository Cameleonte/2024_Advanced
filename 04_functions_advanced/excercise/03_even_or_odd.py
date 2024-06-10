def even_odd(*args):
    nums, command = args[:-1], args[-1:]
    if command[0] == 'even':
        even_nums = list(filter(lambda a: a if a % 2 == 0 else None, nums))
        return even_nums
    elif command[0] == 'odd':
        odd_nums = list(filter(lambda a: a if a % 2 != 0 else None, nums))
        return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
