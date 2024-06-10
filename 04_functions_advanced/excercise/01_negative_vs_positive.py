def main(*args):
    sum_positive_nums = sum([x for x in args if x >= 0])
    sum_negative_nums = sum([y for y in args if y < 0])
    return sum_negative_nums, sum_positive_nums


neg_sum, positive_sum = main(*[int(a) for a in input().split()])

print(f'{neg_sum}\n{positive_sum}')

if positive_sum > abs(neg_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
