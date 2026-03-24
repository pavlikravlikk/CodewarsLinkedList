from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise IndexError("Invalid index or empty list.")    
    current_index = 0
    current_node = node
    while current_node is not None:
        if current_index == index:
            return current_node      
        current_node = current_node.next
        current_index += 1
    raise IndexError("Index out of bounds.")
  
