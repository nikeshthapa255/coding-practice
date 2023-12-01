class TrieNode:
    def __init__(self, value):
        self.value = value
        self.nodes = {} # {[key: string]: Trie}
    def __str__(self):
        return f'{self.value}, {len(self.nodes)}'

"""
* start point
# end point
"""
START_PH = '*'
END_PH = '#'
class Trie:
    def __init__(self):
        self.trie = TrieNode(START_PH)
    
    def insert(self, value):
        curr = self.trie
        for ch in value:
            if ch not in curr.nodes:
                # create new node
                new_node = TrieNode(ch)
                curr.nodes[ch] = new_node
            curr = curr.nodes[ch]
        curr.nodes[END_PH] = TrieNode(END_PH)
    
    def debug_trie(self):
        curr = self.trie
        def dfs(root, lv=0):
            print('node:\t', root, '\t', lv)
            for node in root.nodes.values():
                dfs(node, lv + 1)
        dfs(curr)
        print('****************')

    def _get_node(self, value):
        curr = self.trie
        for ch in value:
            if ch in curr.nodes:
                curr = curr.nodes[ch]
            else:
                return False
        return curr

    def search(self, value):
        # return True or False 
        last_node = self._get_node(value)
        return END_PH in last_node.nodes if last_node else False

        
    
    def starts_with(self, value):
        last_node = self._get_node(value)
        return True if last_node else False

trie = Trie()
trie.debug_trie()
trie.insert('ann')
trie.insert('anne')
trie.insert('any')
trie.debug_trie()
assert trie.starts_with('an') == True

assert trie.starts_with('ad') == False

# test search
assert trie.search('any') == True

assert trie.search('an') == False