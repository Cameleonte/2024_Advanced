import os


def action_manager(operation, my_file, *arg):
    try:
        if operation == 'Replace':
            old_string, new_string = arg[0], arg[1]
            with open(f'{my_file}', 'r+') as existing_file:
                content = existing_file.read()
                existing_file.seek(0)
                existing_file.truncate(0)
                existing_file.write(content.replace(old_string, new_string))
        elif operation == "Delete":
            os.remove(f'{my_file}')
    except FileNotFoundError:
        return f"An error occurred"


while True:
    command = input()
    if command == 'End':
        break
    action, file, *args = command.split('-')
    if action == 'Create':
        open(f'{file}', 'w').close()
    elif action == 'Add':
        with open(f'{file}', 'a') as new_file:
            new_file.write(f'{args[0]}\n')
    else:
        result = action_manager(action, file, *args)
        print(result) if result else None
