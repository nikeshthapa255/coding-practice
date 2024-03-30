"""
MKAverage class:
MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.

"""

class StackHelper:
    def __init__(self):
        self.stack = []
    
    def add_value(self, num: int):
        self.stack.append(num)
    
    def get_last_k(self, k: int):
        length = len(self.stack)
        if length < k: return -1
        return self.stack[length - k: length]

    def calculate_average(self, arr: list[int]) -> int:
        return sum(arr)//len(arr)
    
    def remove_k_min_max(self, m: int, k: int):
        arr = self.get_last_k(m)
        if arr == -1: return -1
        sorted_arr = sorted(arr)
        return self.calculate_average(arr[k: len(arr) - k])

        

class MKAverage:
    def __init__(self, m:int, k:int):
        self.m = m
        self.k = k

        if m <= 2*k:
            raise ValueError('Invalid m and k value')
        
        self.stack_helper = StackHelper()

    def addElement(self, num: int): 
        self.stack_helper.add_value(num)

    def calculateMKAverage(self) -> int:
        # valid stack exists
        return self.stack_helper.remove_k_min_max(self.m, self.k)



mk_obj = MKAverage(5, 2)
mk_obj.addElement(1)
mk_obj.addElement(2)
assert mk_obj.calculateMKAverage() == -1
mk_obj.addElement(3)
mk_obj.addElement(4)
mk_obj.addElement(5)
assert mk_obj.calculateMKAverage() == 3