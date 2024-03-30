from sortedcontainers import SortedList
from collections import deque

class StackHelper:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque([])  # Store the last m values
        self.sorted_list = SortedList()  # This will maintain our values in sorted order
        self.sum_m = 0  # Sum of the last m values
        self.sum_k_min = 0  # Sum of the k smallest values among the last m
        self.sum_k_max = 0  # Sum of the k largest values among the last m

    def add_value(self, num: int):
        """Add a number to the stream, maintaining the balanced binary search tree properties."""
        # When the queue exceeds size m, remove the oldest element
        if len(self.queue) == self.m:
            oldest = self.queue.popleft()
            self.sum_m -= oldest
            self.sorted_list.remove(oldest)  # Remove the oldest value from sorted list
            # Adjust k_min and k_max sums if necessary
            if oldest <= self.sorted_list[self.k - 1]:
                self.sum_k_min -= oldest
                self.sum_k_min += self.sorted_list[self.k - 1]
            if oldest >= self.sorted_list[-self.k]:
                self.sum_k_max -= oldest
                self.sum_k_max += self.sorted_list[-self.k]
        
        # Add the new value
        self.queue.append(num)
        self.sum_m += num
        self.sorted_list.add(num)  # Insert the new value, maintaining order

        # Ensure that sum_k_min and sum_k_max are accurate
        if len(self.sorted_list) > self.k:
            self.sum_k_min = sum(self.sorted_list[:self.k])
            self.sum_k_max = sum(self.sorted_list[-self.k:])
    
    def calculate_mk_average(self) -> int:
        """Calculate and return the MKAverage."""
        if len(self.queue) < self.m:
            return -1  # Not enough elements to compute the average
        return (self.sum_m - self.sum_k_min - self.sum_k_max) // (self.m - 2 * self.k)


class MKAverage:

    def __init__(self, m:int, k:int):
        self.m = m
        self.k = k

        if m <= 2*k:
            raise ValueError('Invalid m and k value')
        
        self.stack_helper = StackHelper(m, k)

    def addElement(self, num: int): 
        self.stack_helper.add_value(num)

    def calculateMKAverage(self) -> int:
        # valid stack exists
        return self.stack_helper.calculate_mk_average()
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()