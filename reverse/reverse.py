class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def remove_head(self):
        if self.head.next_node:
            self.head = self.head.next_node
        else:
            self.head = None

    def reverse_list(self, node, prev):
        new_linked_list = LinkedList()
        current_node = self.head
        while current_node:
            self.remove_head()
            new_linked_list.add_to_head(current_node.value)
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                current_node = None
            self.head = new_linked_list.head
