import os

files = {}
directory = '../'


def find_files(folder, level):
    if level < 0:
        return
    for el in os.listdir(folder):
        current_path = os.path.join(folder, el)
        if os.path.isfile(current_path):
            extension = os.path.splitext(el)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(el)
        else:
            find_files(current_path, level - 1)


find_files(directory, 1)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, filenames in sorted(files.items()):
        output_file.write(f'{ext}\n')
        for file_name in sorted(filenames):
            output_file.write(f'- - -{file_name}\n')
