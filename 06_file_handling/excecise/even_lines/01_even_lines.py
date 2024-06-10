with open('text.txt') as file:
    lst_lines = file.readlines()
    even_lines_list = [lst_lines[line] for line in range(len(lst_lines)) if line % 2 == 0]
    symbols = "-,.!?"
    for symbol in symbols:
        even_lines_list = [row.replace(symbol, '@') for row in even_lines_list]
    [print(' '.join(reversed(row.split()))) for row in even_lines_list]
