def sorting_cheeses(**kwargs):
    sorted_items = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    for cheese, qty in sorted_items:
        result += f"{cheese}\n"
        sorted_qty = sorted(qty, reverse=True)
        for num in sorted_qty:
            result += f"{num}\n"

    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
