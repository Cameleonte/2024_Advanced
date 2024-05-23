from collections import deque

bees_num = deque(int(x) for x in input().split())
nectar_qty = [int(y) for y in input().split()]
symbols = deque(input().split())

tot_honey = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 0
}

while bees_num and nectar_qty:
    if bees_num[0] <= nectar_qty[-1]:
        tot_honey += abs(operations[symbols.popleft()](bees_num.popleft(), nectar_qty.pop()))
    else:
        nectar_qty.pop()

print(f'Total honey made: {tot_honey}')
print(f"Bees left: {', '.join(str(x) for x in bees_num)}") if bees_num else None
print(f"Nectar left: {', '.join(str(x) for x in nectar_qty)}") if nectar_qty else None
