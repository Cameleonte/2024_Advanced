def age_assignment(*args, **kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        for name in args:
            if name.startswith(key):
                new_dict[name] = value
    new_sorted_dict = dict(sorted(new_dict.items(), key=lambda kvp: kvp[0]))
    return '\n'.join(f"{item[0]} is {item[1]} years old." for item in new_sorted_dict.items())


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

print(age_assignment("Peter", "George", G=26, P=19))

