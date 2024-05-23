from collections import deque

user_input = deque(input())
opening = '{[('
closing = '}])'
counter = 0

while user_input and counter < len(user_input) / 2:
    if user_input[0] in closing:
        break
    index = opening.index(user_input[0])
    if user_input[1] == closing[index]:
        user_input.popleft()
        user_input.popleft()
        user_input.rotate(counter)
        counter = 0
    else:
        user_input.rotate(-1)
        counter += 1

print('NO') if user_input else print('YES')
