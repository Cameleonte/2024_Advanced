def add_remove_first(lst_data, action, set_one):
    values_set = [int(elm) for elm in lst_data if elm.isdigit()]
    if action == 'Add':
        values_set = set(values_set)
        set_one = set_one | values_set
    elif action == 'Remove':
        for index in range(len(values_set)):
            if values_set[index] in set_one:
                set_one.remove(values_set[index])
    return set_one


def add_remove_second(lst_data, action, set_two):
    values_set = [int(elm) for elm in lst_data if elm.isdigit()]
    if action == 'Add':
        if action == 'Add':
            values_set = set(values_set)
            set_two = set_two | values_set
    elif action == 'Remove':
        for index in range(len(values_set)):
            if values_set[index] in set_two:
                set_two.remove(values_set[index])
    return set_two


def main(set1, set2):
    for _ in range(int(input())):
        lst_data = [elem for elem in input().split()]
        current_command, num_set = lst_data[0], lst_data[1]
        if len(lst_data) == 2:
            if set1.issubset(set2) or set2.issubset(set1):
                print(True)
            else:
                print(False)
        if num_set == 'First':
            set1 = add_remove_first(lst_data, current_command, set1)
        elif num_set == 'Second':
            set2 = add_remove_second(lst_data, current_command, set2)
    return set1, set2


first_set = {int(num) for num in input().split()}
second_set = {int(num) for num in input().split()}

first_set, second_set = main(first_set, second_set)
print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
