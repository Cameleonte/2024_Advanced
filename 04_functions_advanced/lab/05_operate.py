from functools import reduce


# def operate(operator, *args):
#     mapper = {
#         '+': lambda a, b: a + b,
#         '-': lambda a, b: a - b,
#         '*': lambda a, b: a * b,
#         '/': lambda a, b: a / b
#     }
#     result = 0
#     for sign in mapper.keys():
#         if sign == operator:
#             result = reduce(mapper[sign], args)
#
#     return result

mapper = {
        '+': lambda nums: reduce(lambda a, b: a + b, nums),
        '-': lambda nums: reduce(lambda a, b: a - b, nums),
        '*': lambda nums: reduce(lambda a, b: a * b, nums),
        '/': lambda nums: reduce(lambda a, b: a / b, nums)
    }


def operate(operator, *args):
    return mapper[operator](args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
