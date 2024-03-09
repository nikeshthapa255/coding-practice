def get_count_lt(inp: str) -> str:
    ch, lt = inp.split('[')
    return lt*int(ch)

def is_letter(value: str) -> bool:
    return ord('a')<=ord(value)<=ord('z')

placeholder = ['[', ']']
def is_placeholder(value: str) -> bool: 
    return value in placeholder

def is_digit(value: str) -> bool:
    return not is_letter(value) and not is_placeholder(value)


def decode_string(input_str: str) -> str:
    # single pass approach
    sol = []
    enc_char = []
    enc_count = []
    for lt in input_str:
        # if digit encoding will start
        if is_digit(lt):
            enc_count.append(int(lt))
            enc_char.append('')
            continue
        # close bracker encoding will end
        if is_placeholder(lt):
            if lt == placeholder[1]:

                # decode
                ans = enc_char.pop() * enc_count.pop()
                if (enc_char):
                    enc_char[-1] += ans
                else:
                    sol.append(ans)
                
            continue

        # normal string
        if enc_count:
            enc_char[-1] += lt
        else:
            sol.append(lt)
    #     print(enc_char, enc_count)
    # print(sol)
    return ''.join(sol)

assert decode_string('3[a]bc4[c]d') == 'aaabcccccd'

assert decode_string('3[a]2[bc]') == 'aaabcbc'
assert decode_string('3[a2[c]]') == 'accaccacc'
print(decode_string('3[a2[c]]'))
"""
example 
T 1 - 
3[a]
aaa

3[a]bc4[c]d -> aaabcccccd

3[a, bc4[c, d
3[a]2[bc]
"""


