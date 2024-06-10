class OnlyTextNumbers(Exception):
    """This class handles errors of entering smth else instead of number in letters."""
    pass


def main_input_func(invalid_input=True):
    """Checks if the input is valid else returns the exception"""
    while invalid_input:
        try:
            text = input('Enter a number written in letters in the range zero -> twenty to insert it in a dictionary.'
                         '\nIf you want to continue write "Search": ')
            if text not in valid_insertions:
                raise OnlyTextNumbers
            else:
                invalid_input = False
            return text
        except OnlyTextNumbers:
            print('Insert only numbers as text in the given range!')


numbers_dictionary = {}
valid_insertions = ['Search', 'Remove', 'End', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                    'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']

line = main_input_func()

while line != "Search":
    try:
        number_as_string = line
        number = int(input('Enter the corresponding number as an integer: '))
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    line = main_input_func()

line = input('Enter the searched number written with letters. If you want to continue write "Remove": ')

while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')

    line = input('Enter the searched number written with letters. If you want to continue write "Remove": ')

line = input('Enter the number you want to delete written with letters. '
             'If you want to visualize your dictionary write "End": ')

while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print('Number does not exist in dictionary')

    line = input('Enter the number you want to delete written with letters. '
                 'If you want to visualize your dictionary write "End": ')

print(numbers_dictionary)
