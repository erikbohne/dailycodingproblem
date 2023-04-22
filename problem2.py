"""
april 21th 2023

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None:
        return "null"
    else:
        return root.val + "," + serialize(root.left) + "," + serialize(root.right)
    
def deserialize(string):
    def helper(node_values):
        if not node_values:
            return None

        val = node_values.pop(0)
        if val == "null":
            return None

        node = Node(val)
        node.left = helper(node_values)
        node.right = helper(node_values)
        return node

    node_values = string.split(',')
    return helper(node_values)
    

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'