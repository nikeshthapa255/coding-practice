
class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_ll(root):
    curr = root
    while curr:
        print('node: \t', curr.value)
        curr = curr.next
    
# root: LLNode
def reverse_ll(root):
    curr = root
    prev = None
    while curr.next:
        next_pos = curr.next
        curr.next = prev
        prev = curr
        curr = next_pos
    else:
        # for last node
        curr.next = prev
    return curr


ll = LLNode(1)
ll.next = LLNode(2)
ll.next.next =LLNode(3)
ll.next.next.next = LLNode(4)
print_ll(ll)

rLL = reverse_ll(ll)
print_ll(rLL)



