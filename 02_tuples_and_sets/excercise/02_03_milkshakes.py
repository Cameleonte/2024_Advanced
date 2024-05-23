from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk_cups = deque([int(y) for y in input().split(', ')])

shakes = 0

while chocolates and milk_cups and shakes < 5:
    if chocolates[-1] <= 0 or milk_cups[0] <= 0:
        chocolates.pop() if chocolates[-1] <= 0 else None
        milk_cups.popleft() if milk_cups[0] <= 0 else None
    elif chocolates[-1] == milk_cups[0]:
        shakes += 1
        chocolates.pop()
        milk_cups.popleft()
    else:
        milk_cups.append(milk_cups.popleft())
        chocolates[-1] -= 5

print('Great! You made all the chocolate milkshakes needed!') if shakes == 5 else print('Not enough milkshakes.')

print(f'Chocolate: {", ".join(str(x) for x in chocolates)}') if chocolates else print('Chocolate: empty')

print(f'Milk: {", ".join(str(x) for x in milk_cups)}') if milk_cups else print('Milk: empty')
