def sum_of_factors(num: int) -> int:
    f_sum = 1
    curr = 2
    while curr * curr <= num:
        if num%curr == 0:
            f_sum += curr
            f_sum += (num//curr)
        curr += 1
    return f_sum

assert sum_of_factors(10) == 8
assert sum_of_factors(284) == 220
assert sum_of_factors(220) == 284

def is_amicable(num: int,):
    """
    sum_of_factors(a) = b
    sum_of_factors(b) = a
    """
    f_sum = sum_of_factors(num)
    return sum_of_factors(f_sum) == num


def find_pair():
    ans = set()
    for val in range(1, 10001):
        if val in ans: continue
        if is_amicable(val):
            ans.add(val)
            ans.add(sum_of_factors(val))
    return sum(list(ans))


print(find_pair())