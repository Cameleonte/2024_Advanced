from collections import deque

food_qty = int(input())

tot_orders = deque(list(map(int, (input().split()))))

print(max(tot_orders))

while tot_orders:
    if tot_orders[0] <= food_qty:
        current_order = tot_orders.popleft()
        food_qty -= current_order
    else:
        break

if tot_orders:
    print('Orders left: ', end='')
    for qty in tot_orders:
        print(qty, end=' ')
else:
    print('Orders complete')

# else:
#     print('Orders left: ', *tot_orders)
#     break
#
# else:
#     print('Orders complete')
