def even_odd_filter(**kwargs):
    sum_dict = {}
    if 'odd' in kwargs.keys():
        odd_dict = {'odd': [num for num in kwargs['odd'] if num % 2 != 0]}
        sum_dict.update(odd_dict)
    if 'even' in kwargs.keys():
        even_dict = {'even': [num for num in kwargs['even'] if num % 2 == 0]}
        sum_dict.update(even_dict)
    a = 4
    return dict(sorted(sum_dict.items(), key=lambda kvp: -len(kvp[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))
