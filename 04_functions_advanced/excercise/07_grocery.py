def grocery_store(**kwargs):
    to_print = ''
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    for tup in sorted_result:
        to_print += f'{tup[0]}: {tup[1]}\n'

    return f'{to_print}'


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
