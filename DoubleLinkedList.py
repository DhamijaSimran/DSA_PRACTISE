class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList():

    def __init__(self):
        self.head = None
        self.len = 0

    # insert at beginning
    def insertAtBeginning(self, val):
        first_node = self.head
        node = Node(val)
        node.next = first_node
        node.prev = None
        if first_node is not None:
            first_node.prev = node
        self.head = node

    def insertAtEnd(self, val):
        node = Node(val)
        temp = self.head

        if temp is None:
            node.next = self.head
            node.prev = None
            self.head = node
            return

        while temp.next is not None:
            temp = temp.next

        temp.next = node
        node.prev = temp

    # insert before node
    def insertAtPos(self, pos, val):

        if pos == 0:
            self.insertAtBeginning(val)
            return

        if pos == self.len:
            self.insertAtEnd(val)
            return

        node = Node(val)
        cnt = 1
        temp = self.head

        # remember to update before pointer of temp
        # if temp.next is at pos number then
        # temp is the pointer before temp.next
        # temp.next will shift to pos+1, new node will come to pos
        # thus node.next=temp.next
        # update node.prev to temp
        # now update temp.next prev nodes
        # temp.next will have prev as node, temp.next.prev=node
        # temp.next might be null in case temp is last node.
        # update temp.next to node
        while temp.next is not None:
            if cnt == pos:
                node.next = temp.next
                node.prev = temp
                if temp.next is not None:
                    temp.next.prev = node
                temp.next = node
                break
            cnt += 1
            temp = temp.next

    def insertBeforeNode(self, node_val, val):
        temp = self.head
        node = Node(val)

        # if temp is the node before which insertion has to be done
        # then temp.prev is the node before temp
        # then node.next=temp and node.prev=temp.prev
        # and temp.prev will point to new node
        # temp.prev.next=node
        # and temp will have prev pointer as node
        # temp.prev=node
        while temp is not None:
            if temp.value == node_val:
                node.next = temp
                node.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = node
                    temp.prev = node
                else:
                    self.head = node
                return
            temp = temp.next

    def insertAfterNode(self, node_val, val):
        temp = self.head
        node = Node(val)

        while temp is not None:
            if temp.value == node_val:
                node.next = temp.next
                node.prev = temp
                if temp.next is not None:
                    temp.next.prev = node
                    temp.next = node
                return
            temp = temp.next

    def deleteFirstNode(self):
        # move head to next node
        # make the next node's prev point to None
        self.head = self.head.next
        self.head.prev = None

    def deleteAllDLL(self):
        self.head = None

    def deleteNodeWithVal(self, val):
        temp = self.head
        # delete temp
        # make temp.prev point to temp.next
        # make temp.next point to temp.prev
        while temp is not None:
            if temp.value == val:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.deleteFirstNode()
                if temp.next is not None:
                    temp.next.prev = temp.prev
                else:
                    self.deleteLastNode()
            temp = temp.next

    def deleteLastNode(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    def reverseList(self):
        temp = self.head
        current = None
        # reversing DLL - make the next pointer point to prev node
        # and prev pointer point to next node
        # head pointer will become last node, so it will have next pointer as null
        # and prev pointer as 2nd node
        # last pointer will become 1st node, so it will have prev pointer as null
        # and next pointer as 2nd node
        # so we need 2 pointers to maintain the next and prev nodes
        # at end, temp will be none and current will be 2nd last node
        # as when temp is none, the while loop wont execute and current
        # will remain as 2nd last node
        # current.prev will be pointing to the next nodes of the list
        # so head points to current.prev
        # check for current=null in DLLs with 1/2 nodes
        while temp is not None:
            current = temp.prev
            temp.prev = temp.next
            temp.next = current
            temp = temp.prev

        if current is not None:
            self.head = current.prev

    def traverseList(self):
        temp = self.head
        rep = ""
        self.len = 0
        while temp is not None:
            self.len += 1
            rep += str(temp.value) + "-->"
            temp = temp.next

        rep += "None"
        print(rep)
        print("Linked list length " + str(self.len))


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insertAtBeginning(5)
    dll.insertAtBeginning(6)
    dll.insertAtBeginning(7)
    dll.insertAtBeginning(8)
    dll.traverseList()

    dll.insertAtEnd(10)
    dll.insertAtEnd(99)
    dll.insertAtEnd(100)
    dll.traverseList()

    dll.insertAtPos(1, 88)
    dll.traverseList()
    dll.insertAtPos(3, 38)
    dll.traverseList()
    dll.insertAtPos(9, 38)
    dll.traverseList()

    dll.insertBeforeNode(7, 45)
    dll.traverseList()
    dll.insertBeforeNode(38, 33)
    dll.traverseList()
    dll.insertBeforeNode(8, 0)
    dll.traverseList()

    dll.insertAfterNode(7, 45)
    dll.traverseList()
    dll.insertAfterNode(38, 45)
    dll.traverseList()

    dll.deleteFirstNode()
    dll.traverseList()

    dll.deleteLastNode()
    dll.traverseList()

    dll.deleteNodeWithVal(38)
    dll.traverseList()
    dll.deleteNodeWithVal(45)
    dll.traverseList()
    dll.deleteNodeWithVal(7)
    dll.traverseList()
    dll.deleteNodeWithVal(100)
    dll.traverseList()

    print("reversing list")
    dll.reverseList()
    dll.traverseList()
