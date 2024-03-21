from bisect import bisect_left as bl, bisect_right as br
class RangeModule:

    def __init__(self):
        self.range = [] # [left, right] even - left, odd - right


    def addRange(self, left: int, right: int) -> None:
        l_idx, r_idx = bl(self.range, left), br(self.range, right)
        self.range[l_idx: r_idx] = [left]*(l_idx%2 == 0) + [right]*(r_idx%2 == 0)


        

    def queryRange(self, left: int, right: int) -> bool:
        l_idx, r_idx = br(self.range, left), bl(self.range, right)
        return l_idx == r_idx and l_idx%2 == 1

        

    def removeRange(self, left: int, right: int) -> None:
        l_idx, r_idx = bl(self.range, left), br(self.range, right)
        self.range[l_idx: r_idx] = [left]*(l_idx%2 == 1) + [right]*(r_idx%2 == 1)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)