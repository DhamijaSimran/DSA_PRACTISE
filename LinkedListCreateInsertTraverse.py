# generic node object
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    # below init method will overwrite the first one.
    # in java, we could overload the constructor
    # but cant do that in python
    # def __init__(self, value):
    #     self.value = value

# create LL here, add head pointer and more.
class linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current is not None:
                print(current.data)
                current = current.next

    def prepend_node(self, data):
        node = Node(data)
        if self.head is not None:
            print("List is empty. Adding first Node")
            self.head = node
        else:
            node.next = self.head.next
            self.head = node

    def append_node(self, data):
        node = Node(data)
        if self.head is None:
            print("List is empty. Adding first Node")
            self.head = node
        else:
            current = self.head
            while current is not None:
                current = current.next
            current.next = node
            node.next = None

    def insert_at_pos(self, data, pos):
        node = Node(data)
        if pos == 0:
            self.head = node
        else:
            ind = 0
            cur = self.head
            while cur.next is not None:
                cur = cur.next
                ind += 1

            prev.next = node
            node.next = cur

if __name__ == "__main__":
    pass


