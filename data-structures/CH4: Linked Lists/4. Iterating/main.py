from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head

        while current_node is not None:
            yield current_node
            current_node = current_node.next

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
