import re

with open('text.txt') as file:
    lines_to_transfer = file.read().split('\n')
    symbols = {}
    for line in lines_to_transfer:
        letters_count = len(''.join(re.findall(r"\w", line)))
        punctuation_marks_count = len(''.join(re.findall(r"[^\s\w]", line)))
        symbols[lines_to_transfer.index(line) + 1] = (letters_count, punctuation_marks_count)

with open('output.txt', 'w') as f:
    for key, value in symbols.items():
        f.write(f'Line {key}: {lines_to_transfer[key - 1]} {value}\n')
