from collections import deque

expression = input().split()
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

numbers = deque()
for elem in expression:
    if elem in '*,/,+,-':
        while len(numbers) > 1:
            result = operations[elem](numbers.popleft(), numbers.popleft())
            numbers.appendleft(result)
    else:
        numbers.append(int(elem))

print(*numbers)
