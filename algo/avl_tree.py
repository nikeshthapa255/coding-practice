is_debug = True

def debug(*args, **kwargs):
    if is_debug: print(*args, **kwargs) 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.root = None


def create_node(value):
    return Node(value)

def show_tree(root):
    if (not is_debug): return
    debug('*************\nShow tree')
    def recur_tree(node):
        print(node.value, node.height)
        if node.left:
            debug('l-', end='')
            recur_tree(node.left)

        if node.right:
            debug('r-', end='')
            recur_tree(node.right)
    recur_tree(root)
    debug('*************')

def get_height(node):
    return 0 if node == None else node.height

def recalculate_height(node):
    if not node: return 0
    l_h = get_height(node.left)
    r_h = get_height(node.right)
    node.height = max(l_h, r_h)
    return node.height

def get_balance_value(node):
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return left_height - right_height

# insertion
def insert_val(new_value, root):
    new_node = create_node(new_value)
    depth_stack = []
    current = root
    debug('i0', current.value)
    while current.left or current.right:
        debug('i1', current.value)
        depth_stack.append(current)
        if current.left and new_value <= current.value:
            current = current.left
        elif current.right and new_value > current.value:
            current = current.right
        else:  break
    else:
        debug('i2', current.value, new_value)
        depth_stack.append(current)
        current.height += 1
        if new_value <= current.value:
            current.left, new_node.root = new_node, current
        else:
            current.right, new_node.root = new_node, current

    for node in depth_stack[::-1]:
        # check height
        recalculate_height(node)
        b_value = get_balance_value(node)

def recal_after_balance(node):
    recalculate_height(node.left)
    recalculate_height(node.right)
    recalculate_height(node)

def update_parent(node, parent):
    if parent:
        if parent.value > node.value: parent.left = node
        else: parent.right = node

def ll_rotate(node):
    l_n = node.left
    ll_n = node.left.left
    # l_n is new parent of ll and node
    debug(node.value, l_n.value, ll_n.value)
    l_n.right, node.left = node, l_n.right
    update_parent(l_n, node.root)
    recal_after_balance(l_n)

def lr_rotate(node):
    l_n = node.left
    lr_n = node.left.right
    # lr_n is the new root
    lr_n.left, lr_n.right, l_n.right, node.left = l_n, node, lr_n.left, lr_n.right
    update_parent(lr_n, node.root)
    recal_after_balance(lr_n)


def rr_rotate(node):
    r_n = node.right
    rr_n = node.right.right
    # r_n is new parent of rr and node
    debug(node.value, r_n.value, rr_n.value)
    r_n.left, node.right = node, l_n.left
    update_parent(r_n, node.root)
    recal_after_balance(r_n)

def rl_rotate(node):
    r_n = node.right
    rl_n = node.right.left
    # rl new root
    rl_n.left, rl_n.right, node.right, r_n.left = node, r_n, rl_n.left, rl_n.right
    update_parent(rl_n, node.root)
    recal_after_balance(rl_n)



# check 
def balance_node(node):
    b_val = get_balance_value(node)
    if b_val > 1:
        # ll or lr case
        ll_height = get_height(node.left.left)
        lr_height = get_height(node.left.right)
        if ll_height > lr_height:
            # ll case
            ll_rotate(node)
        else:
            # lr case
            lr_rotate(node)
    elif b_val < -1:
        # rr or lr case
        rr_height = get_height(node.right.right)
        rl_height = get_height(node.right.left)
        if rr_height > rl_height:
            # rr
            rr_rotate(node)
            # rl
            rl_rotate(node)

        
def avl(val_arr):
    arr_g = (val for val in val_arr)

    root_node = create_node(next(arr_g))
    for val in arr_g:
        debug('insert', val)
        insert_val(val, root_node)
        show_tree(root_node)
    return root_node
    



# Test cases
a = Node(10)
assert a.value == 10

a = [5, 3, 1, 6, 7, 8, 9, 10]
avl(a)