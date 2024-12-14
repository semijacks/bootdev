from node import Node

class LinkedList:
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return

            # Use the __iter__ method to find the last node
        tail = None
        for current_node in self:
            tail = current_node

        tail.next = node

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head

        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)