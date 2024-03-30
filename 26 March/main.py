
def mergeArray(a: list[int], b: list[int]):
    c = []
    al, bl = len(a), len(b)
    ai, bi = 0, 0
    while ai < al and bi < bl:
        if a[ai] < b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1
    
    while ai<al:
        c.append(a[ai])
        ai += 1
    
    while bi<bl:
        c.append(b[bi])
        bi += 1
    
    return c


assert mergeArray([1,2,3], [2, 5, 5]) == [1, 2, 2, 3, 5, 5]