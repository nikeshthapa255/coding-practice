

def k_subsequence(s, k):
    # count the letters
    count = {}
    for chr in s:
        if chr not in count: count[chr] = 0
        count[chr] += 1
    
    count_arr = [[key, value] for key, value in count.items()]
    count_arr.sort(key = lambda x: -x[1])
    print(count_arr)

    # if unqique letter are less than k, then no solution case
    if len(count_arr) < k: return 0

    # get the last k values letters
    sol_arr = count_arr
    print('sol arr', sol_arr)

    # create batch for each count numbers
    batch = []
    for ch, c1 in sol_arr:
        if len(batch) == 0:
            batch.append([ch])
        else:
            if count[batch[-1][0]] == c1:
                batch[-1].append(ch)
            else:
                batch.append([ch])

    print('batch ', batch) 

    # if we need x and we have N letters than do nCx 
    ans = 1
    md = 10**9 + 7
    curr_k = k
    for ch_batch in batch:
        if curr_k == 0 :break
        b_len = len(ch_batch)
        c1 = count[ch_batch[0]]
        print(b_len, c1)
        if b_len <= curr_k:
            curr_k -= b_len
            ans = (ans*(c1 ** b_len))%md
        else:
            r = b_len - curr_k
            n = b_len
            curr_k = 0
            ans = (ans*(c1 ** r)*ncr(n, r, md))%md
    return ans

         



ex1 = 'aabbcddd'
print(k_subsequence(ex1, 2))
