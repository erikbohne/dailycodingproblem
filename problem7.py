"""
april 26th 2023

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unival_trees(node):
    _, count = helper(node)
    return count


def helper(node):
    if node is None:
        return True, 0

    left_unival, left_count = helper(node.left)
    right_unival, right_count = helper(node.right)
    total_count = left_count + right_count

    if left_unival and right_unival:
        if node.left is not None and node.left.val != node.val:
            return False, total_count
        if node.right is not None and node.right.val != node.val:
            return False, total_count
        return True, total_count + 1
    return False, total_count


node0 = Node(0)
node1 = Node(1)
node2 = Node(0)
node3 = Node(1)
node4 = Node(0)
node5 = Node(1)
node6 = Node(1)

node0.left = node1
node0.right = node2

node2.left = node3
node2.right = node4

node3.left = node5
node3.right = node6

print(count_unival_trees(node0))