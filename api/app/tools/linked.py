class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class Linked:

    def __init__(self):
        self.head = None
        self.data = []

    def add(self, index, data):
        self.data.insert(index, data)

    def remove(self, index):
        pass

    def clear(self):
        pass

    def size(self):
        pass

    def empty(self):
        pass

    def search(self, index):
        pass

    def get_all(self):
        return self.data


if __name__ == '__main__':
    node = Node('a')
    print(node.next)
    print(node.data)
    s1 = "hello"
    print(len(s1))
    print(s1.count('l'))
