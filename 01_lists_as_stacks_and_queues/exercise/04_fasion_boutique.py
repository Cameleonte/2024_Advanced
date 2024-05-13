clothes_received = list(map(int, input().split()))
rack_capacity = int(input())

stack_clothes = clothes_received
sum_pieces = 0
tot_racks_needed = 0


while stack_clothes:
    next_piece = stack_clothes[-1]
    if next_piece + sum_pieces <= rack_capacity:
        sum_pieces += stack_clothes.pop()
        if len(stack_clothes) == 1 and sum_pieces != 0:
            tot_racks_needed += 1
    else:
        sum_pieces = 0
        tot_racks_needed += 1

print(tot_racks_needed)
