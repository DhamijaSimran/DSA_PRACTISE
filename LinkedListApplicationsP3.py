import copy


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
        temp = copy.deepcopy(self.head)
        while temp is not None:
            repr += str(temp.value) + "-->"
            self.len += 1
            temp = temp.next
        repr += "None"
        print(repr)

    def createLL(self):
        nodes = [Node(i) for i in range(1, 8)]
        self.head = nodes[0]
        for i in range(0, 6):
            nodes[i].next = nodes[i + 1]
        nodes[6].next = None

    def createLoop(self):
        temp = self.head
        count = 0

        while temp.next is not None:
            count += 1
            if count == 6:
                print("creating loop from last node to " + str(count) + " position.")
                temp2 = temp
            temp = temp.next

        # here we are at last node. make it point to any other node
        # the other node is temp2
        temp.next = temp2
        print("last node now  points to " + str(temp.next.value))

    def detectLoop(self):
        # Floyd tortoise and hare algorithm
        # https://stackoverflow.com/questions/2936213/how-does-finding-a-cycle-start-node-in-a-cycle-linked-list-work/6110767#6110767
        slow = self.head
        fast = self.head

        if slow is None or slow.next is None:
            print("Not enough nodes in LL to have cycle")
            return

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            # check if fast and slow have the SAME ADDRESS
            # NOT IF THEY HAVE THE SAME VALUE
            if fast == slow:
                print("Loop detected in Linked List")
                # print(fast.value, slow.value)
                break

        # find length of loop
        if fast == slow:
            len = 1
            # print(fast.value,slow.value)
            while fast.next is not slow:
                # print(fast.value, slow.value)
                fast = fast.next
                len += 1
            print("length of loop = " + str(len))
            print("Removing Loop")
            self.removeLoop(len)

    # https://afteracademy.com/blog/detect-and-remove-loop-in-a-linked-list
    def removeLoop(self, len):
        ptr1 = self.head
        ptr2 = self.head

        while len > 0:
            ptr2 = ptr2.next
            len -= 1

        print("ptr2 at " + str(ptr2.value))

        # move ptr1 and ptr2 by 1
        # ptr2 already in loop and will keep circling
        # ptr1 will come in loop
        # they will meet eventually
        # if both ptr1 and ptr2 point to same node
        # then we have found start of the loop
        while ptr1.next is not ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # remove loop
        # ptr2 points to end of LL
        # ptr1 points to beginning of cycle
        ptr2.next = None

    def getMiddle(self):
        # we can do this easily if we know the length of linked list
        # beforehand. we have to halve the length then traverse upto
        # that node.
        # this method assumes length is not known beforehand.
        count = 0
        temp = self.head
        middle = self.head
        while temp is not None:
            count += 1
            if count % 2 == 0:
                middle = middle.next
            temp = temp.next

        print("Middle of Linked List is the node with value " + str(middle.value))

    def removeKFromEnd(self, k):
        # nth node from end will be (l-n)th node from head
        # where l is length of linked list
        # we can find nth node from beginning easily, by traversing upto n
        # take 2 pointers, first one at head and second one at nth node
        # now we can traverse (l-n) distance by moving each pointer by 1
        # till second one reaches the end. first one would be pointing to l-n node
        # which would be nth node from end
        m = k
        ptr1 = self.head
        ptr2 = self.head
        prev = None
        while k > 0:
            ptr2 = ptr2.next
            k -= 1

        while ptr2 is not None:
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        print(str(m) + " node from end is " + str(ptr1.value))
        # delete this node
        prev.next=ptr1.next
        ptr1.next=None


if __name__ == "__main__":
    LL = LinkedList()
    print("Creating Linked List")
    LL.createLL()
    LL.__repr__()

    print("Creating Loop")
    LL.createLoop()
    # LL.__repr__()

    print("Detecting Loop")
    LL.detectLoop()
    LL.__repr__()

    print("Finding middle of Linked List")
    LL.getMiddle()

    print("Deleting kth node from end")
    LL.removeKFromEnd(5)
    LL.__repr__()
