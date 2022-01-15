class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

    # type Node in terminal, get this value
    def __repr__(self):
        return str(self.value) + "->" + str(self.next)


class LinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    # representation of LinkedList class
    # type name of LinkedList object and see
    # result of this method
    def __repr__(self):
        node = self.head
        rep = ""
        while node is not None:
            rep += (str(node.value) + "->")
            node = node.next
        rep += "None"
        return rep

    def createLL(self):
        m = Node(1)
        n = Node(2)
        o = Node(3)
        p = Node(4)
        q = Node(5)

        self.head = m
        m.next = n
        n.next = o
        o.next = p
        p.next = q
        q.next = None

    def traverseLLAndUpdateCnt(self):
        start = self.head
        cnt = 0
        while start:
            cnt += 1
            # print(start.value)
            start = start.next

        self.len = cnt
        print("Linked List length " + str(cnt))

    def searchLL(self, val):
        start = self.head
        pos = 0
        while start:
            pos += 1
            if start.value == val:
                print("Found " + str(val) + " at " + str(pos) + " position")
                return
            start = start.next

        print(str(val) + " not found")

    def insertAtBeg(self, val):
        node = Node(val)
        # assume head points to already existing nodes in LL
        node.next = self.head
        self.head = node

    def insertAtEnd(self, val):
        node = Node(val)
        end = None
        start = self.head

        if self.head is None:
            self.head = node
        else:
            while start:
                end = start
                start = start.next
            end.next = node

    def insertAtPos(self, pos, val):
        count = 0
        if pos == count:
            self.insertAtBeg(val)
        elif pos == self.len:
            self.insertAtEnd(val)
        else:
            node = Node(val)
            temp = self.head
            # temp.next will be the node at pos
            # as loop is 'while temp.next'
            # this is because we need temp and temp.next as before and after nodes for linking
            # for node to be at pos, temp.next will be shifted after node
            # thus node.next=temp.next
            # and the node before pos, needs to point to new node
            # thus node.next=temp
            while temp.next:
                count += 1
                if count == pos:
                    node.next = temp.next
                    temp.next = node
                temp = temp.next

    def insertAfterPos(self, pos, val):
        # position after pos will be pos+1
        if self.len == 0:
            self.insertAtBeg(val)
        elif pos == self.len:
            self.insertAtEnd(val)
        else:
            temp = self.head
            node = Node(val)
            count = 0
            while temp.next:
                count += 1
                if count == pos + 1:
                    node.next = temp.next
                    temp.next = node
                    break
                temp = temp.next

            if count < pos:
                print("index out of range")

    def insertAfterNode(self, node_val, val):
        if self.head is None:
            self.insertAtBeg(val)
        else:
            node = Node(val)
            temp = self.head
            while temp.next:
                if temp.value == node_val:
                    node.next = temp.next
                    temp.next = node
                    break
                temp = temp.next

    def insertBeforePos(self, pos, val):
        # position before pos will be pos-1
        if pos == 0:
            self.insertAtBeg(val)
        else:
            node = Node(val)
            temp = self.head
            cnt = 0
            while temp.next:
                if cnt == pos - 1:
                    node.next = temp.next
                    temp.next = node
                    break
                cnt += 1
                temp = temp.next

            if cnt > pos:
                print("index out of range")

    def insertBeforeNode(self, node_val, val):
        # insert before node having node_val as value
        if self.head is None:
            self.insertAtBeg(val)
        else:
            node = Node(val)
            temp = self.head
            while temp.next is not None:
                if temp.next.value == node_val:
                    node.next = temp.next
                    temp.next = node
                    break
                temp = temp.next

    def deleteAllLL(self):
        if self.head is not None:
            self.head = None
        else:
            print("List is empty")

    def deleteAtBeg(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next

            prev.next = None
            # here temp points to the last node
            # as in while loop, temp.next is None at "None" of end of ll
            # so it breaks and temp still points to previous node
            # prev points to the node before temp

    def deleteAtPos(self, node_val):
        # generic,can delete at end and beginning too
        if self.head is None:
            print("List is empty")
        else:
            if node_val == self.head.value:
                self.head = self.head.next
            else:
                temp = self.head
                prev = None
                while temp is not None:
                    if temp.value == node_val:
                        prev.next = temp.next
                    prev = temp
                    temp = temp.next

    def reverseLL(self):
        # main operation: make temp point to prev
        #                 make self.head point to end of list

        prev = None
        node = self.head

        while node is not None:
            # get the node after this one
            after = node.next

            # make this node point to previous one
            node.next = prev

            # update prev to this node
            prev = node

            # move to next node. node=node.next wont work bcos node points to prev now
            node = after

        # node is none here, we have reached end of LL
        # prev will be the last node that is reversed, or last node of original ll
        # thus head points to prev
        self.head = prev


if __name__ == "__main__":
    ll = LinkedList()
    ll.createLL()
    # print(ll.__repr__())
    # ll.traverseLL()
    # ll.searchLL(0)
    print("searchLL(3)")
    ll.searchLL(3)
    print("")

    print("insertAtBeg(9)")
    ll.insertAtBeg(9)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("insertAtEnd(7)")
    ll.insertAtEnd(7)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    # 0 indexed
    print("insertAtPos(2, 94)")
    ll.insertAtPos(2, 94)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("insertAfterPos(200, 78)")
    ll.insertAfterPos(200, 78)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("insertAfterPos(8, 78)")
    ll.insertAfterPos(8, 78)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    # #might fail
    # print("insertAfterPos(5, 34)")
    # ll.insertAfterPos(5, 34)
    # print(ll.__repr__())
    # ll.traverseLLAndUpdateCnt()
    # print("")
    #
    # # might fail
    # print("insertBeforePos(5, 49)")
    # ll.insertBeforePos(5, 49)
    # print(ll.__repr__())
    # ll.traverseLLAndUpdateCnt()
    # print("")

    print("insertAfterNode(7,99)")
    ll.insertAfterNode(7, 99)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("insertAfterNode(9,99)")
    ll.insertAfterNode(9, 99)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("insertBeforeNode(99, 808)")
    ll.insertBeforeNode(99, 808)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("insertBeforeNode(78, 808)")
    ll.insertBeforeNode(78, 808)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("deleteAtEnd()")
    ll.deleteAtEnd()
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("deleteAtPos(808)")
    ll.deleteAtPos(808)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("deleteAtPos(9)")
    ll.deleteAtPos(9)
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")

    print("reverseLL")
    ll.reverseLL()
    print(ll.__repr__())
    ll.traverseLLAndUpdateCnt()
    print("")