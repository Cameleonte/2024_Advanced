queries_count = int(input())

stack = []
for count in range(queries_count):
    query = input().split()
    if query[0] == '1':
        stack.append(int(query[1]))

    else:
        if not stack:
            continue
        if query[0] == '2':
            stack.pop()
        elif query[0] == '3':
            print(max(stack))
        elif query[0] == '4':
            print(min(stack))

# while stack:
#     if len(stack) == 1:
#         print(stack.pop())
#     else:
#         print(stack.pop(), end=', ')

stack.reverse()
print(*stack, sep=", ")
