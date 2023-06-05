class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_from_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_from_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_by_index(self, index):
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0

        while current and count != index:
            prev = current
            current = current.next
            count += 1

        if not current:
            return

        prev.next = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



