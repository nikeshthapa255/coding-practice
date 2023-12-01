
class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0]*(2*size)
    
    # 1 indexed value
    def add_val(self, pos, value):
        idx = pos + self.size
        self.tree[idx] += value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    # 1 indexed [l, r)
    def query(self, l, r):
        # Query the sum in the range [l, r)
        result = 0
        l += self.size
        r += self.size
        while l < r:
            if l % 2:
                result += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                result += self.tree[r]
            l //= 2
            r //= 2
        return result