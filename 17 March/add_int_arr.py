def add(n1: list[int], n2: list[int]):
    num1, num2 = n1[:], n2[:]
    ln1, ln2 = len(num1), len(num2)
    if ln1<ln2: 
        ln1, ln2 = ln2, ln1
        num1, num2 = num2, num1
    extra = 0
    idx = 0 
    while idx < ln1:
        val2 = num2[ln2 - idx - 1] if idx < ln2 else 0
        sm = num1[ln1 - idx - 1] + val2 + extra
        num1[ln1-idx - 1] = sm%10
        extra = sm//10
        idx += 1
    else:
        if extra:
            num1.insert(0, extra)
    return num1

print(add([1, 0, 0, 0], [1,]))