from collections import deque

# my way to resolve:
# def potato_pass(lst, n):
#     if len(lst) == 1:
#         print(f"Last is {lst[0]}")
#         return lst
#     else:
#         for kid in range(1, n + 1):
#             if kid == n:
#                 leaves = lst.popleft()
#                 print(f'Removed {leaves}')
#             else:
#                 kiddo = lst.popleft()
#                 lst.append(kiddo)
#         return potato_pass(lst, n)


# list_kids_names = deque(input().split())
#
# toss = int(input())
#potato_pass(list_kids_names, toss)


list_kids_names = deque(input().split())

toss = int(input()) - 1
while len(list_kids_names) > 1:
    list_kids_names.rotate(-toss)
    remove = list_kids_names.popleft()
    print(f'Removed {remove}')

print(f"Last is {list_kids_names[0]}")
