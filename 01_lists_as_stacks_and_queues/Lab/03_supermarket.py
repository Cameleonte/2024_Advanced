from collections import deque

customer = input()
queue = deque()

while customer != 'End':
    if customer == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(customer)
    customer = input()

print(f'{len(queue)} people remaining.')
