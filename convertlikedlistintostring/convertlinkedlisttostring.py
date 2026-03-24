def stringify(node):
    parts = []
    while node is not None:
        parts.append(str(node.data))
        node = node.next
    parts.append("None") 
    return " -> ".join(parts)
