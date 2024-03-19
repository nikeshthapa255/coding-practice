 def hammingDistance(a):
    counts = [0]*32
    for e in a:
        for i in range(32):
            counts[i] += (e>>i)&1
            
    # print(counts)
    n = len(a)
    res = 0
    for c in counts:
        res += c*(n-c)%1000000007
        
    return 2*res%1000000007