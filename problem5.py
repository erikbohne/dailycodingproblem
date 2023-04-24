"""
april 24th 2023

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, 
which is an XOR of the next node and the previous node. 
Implement an XOR linked list; it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer 
functions that converts between nodes and memory addresses.
"""
import ctypes

class Node:
    def __init__(self, data):
        self.data = data
        self.both = 0
    
class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def get_pointer(self, node):
        return id(node)
    
    def dereference_pointers(self, pointer):
        return ctypes.cast(pointer, ctypes.py_object).value if pointer else None
    
    def xor_pointers(self, a, b):
        return a ^ b
    
    def add(self, element):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            prevPointer = self.get_pointer(self.tail)
            self.tail.both = self.xor_pointers(self.tail.both, self.get_pointer(newNode))
            newNode.both = prevPointer
            self.tail = newNode
        
    def get(self, index):
        prevPointer = 0
        curr = self.head
        for _ in range(index):
            if curr is None:
                return None
            nextPointer = self.xor_pointers(prevPointer, curr.both)
            prevPointer = self.get_pointer(curr)
            curr = self.dereference_pointers(nextPointer)
            
        return curr
    
xor_linked_list = XORLinkedList()

# Add elements to the XOR linked list
xor_linked_list.add("A")
xor_linked_list.add("B")
xor_linked_list.add("C")

# Get elements from the XOR linked list
print(xor_linked_list.get(0).data)  # Output: A
print(xor_linked_list.get(1).data)  # Output: B
print(xor_linked_list.get(2).data)  # Output: C
        
