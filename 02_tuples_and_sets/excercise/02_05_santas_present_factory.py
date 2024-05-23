from collections import deque

materials = [int(a) for a in input().split()]
magic_level = deque(int(b) for b in input().split())

presents = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_presents = {}

while materials and magic_level:
    magic_used, materials_used = magic_level[0], materials[-1]
    tot_magic_level = magic_used * materials_used
    if tot_magic_level in presents.keys():
        if presents[tot_magic_level] not in crafted_presents:
            crafted_presents[presents[tot_magic_level]] = 0
        crafted_presents[presents[tot_magic_level]] += 1
        materials.pop()
        magic_level.popleft()
    elif tot_magic_level < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif tot_magic_level > 0:
        materials[-1] += 15
        magic_level.popleft()
    else:
        if magic_used == 0:
            magic_level.popleft()
        if materials_used == 0:
            materials.pop()

if (('Doll' in crafted_presents and 'Wooden train' in crafted_presents)
        or ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents)):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(str(i) for i in materials[::-1])}')
if magic_level:
    print(f'Magic left: {", ".join(str(a) for a in magic_level)}')
for present, amount in sorted(crafted_presents.items()):
    if amount > 0:
        print(f'{present}: {amount}')
