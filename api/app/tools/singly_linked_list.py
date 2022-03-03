class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return len(tuple(iter(self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        for i, node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index, data):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

    def insert_tail(self, data) -> None:
        self.insert_nth(len(self), data)

    def insert_head(self, data) -> None:
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data) -> None:
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head  # link new_node to head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def print_list(self) -> None:  # print every node data
        print(self)

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):  # delete from tail
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int = 0):
        if not 0 <= index <= len(self) - 1:  # test if index is valid
            raise IndexError("list index out of range")
        delete_node = self.head  # default first node
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data

    def is_empty(self) -> bool:
        return self.head is None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev
