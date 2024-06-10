def concatenate(*args, **kwargs):
    my_string = ''.join(args)
    for key, value in kwargs.items():
        my_string = my_string.replace(key, value)
    return my_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
