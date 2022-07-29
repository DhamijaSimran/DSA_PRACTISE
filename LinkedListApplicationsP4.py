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


    def mergesort_list(self):
        if self.head is None:
            return

        mid = self.get_middle()
        left_list = self.head
        right_list = mid.next
        mid.next=None
        self.mergesort_list(left_list)
        self.mergesort_list(right_list)
        merge_list(left_list,right_list)

    def get_middle(self):
        temp = self.head
        slow = temp
        fast = temp
        while fast is not None and fast.next is not None:
            slow = temp.next
            fast = temp.next.next

        return slow

    def merge_list(self,left_list,right_list):
        new_list=None
        # need to store tail of new list so that we can
        # append to this position
        tail = None
        while left_list is not None and right_list is not None:


    def flattenLL(self):
        pass


if __name__ == "__main__":
    LL = LinkedList()
    LL.createLL()
    LL.__repr__()

    LL.sortLL()
    LL.__repr__()
