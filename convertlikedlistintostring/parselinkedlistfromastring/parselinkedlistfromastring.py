from preloaded import Node

def linked_list_from_string(s):
    parts = s.split(' -> ')  
    head = None
    for val in reversed(parts[:-1]):
        head = Node(int(val), head)       
    return head
