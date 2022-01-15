import random


class Node:
    def __init__(self, value=0):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        repr = ""
        self.len = 0
        temp = self.head
        while temp is not None:
            repr += str(temp.value) + "-->"
            self.len += 1
            temp = temp.next
        repr += "None"
        print(repr)

    def createLL(self):
        nodes = [Node(random.randint(0, 100)) for i in range(1, 11)]
        self.head = nodes[0]
        for i in range(0, 9):
            nodes[i].next = nodes[i + 1]
        nodes[9].next = None

    def sortLL(self):
        beg = self.head
        start = 0
        end = self.len
        # merge sort
        self.call_merge(start, end)

    def call_merge(self, start, end):
        while start < end:
            mid = start + ((end - start) // 2)
            self.call_merge(start, mid)
            self.call_merge(mid + 1, end)
            self.mergesort(start, mid, end)

    def mergesort(self, start, mid, end):
        L = [i for i in range(start, mid + 1)]
        temp = self.head
        # sort first half of linked list
        for i in range(start, mid + 1):

            temp = temp.next
        R = [i for i in range(mid + 1, end + 1)]

    def flattenLL(self):
        pass


if __name__ == "__main__":
    LL = LinkedList()
    LL.createLL()
    LL.__repr__()

    LL.sortLL()
    LL.__repr__()
