class Node:
    def __init__(self, value=0):
        self.next = None
        self.value = value


class CLL:
    def __init__(self):
        self.last = None

    def __repr__(self):
        # get first node
        temp = self.last.next
        repr = ""
        if temp is not None:
            # as its cll, the condition to stop traversing the list is
            # when we reach the last node
            # take the value of first node before the loop enters
            repr += str(temp.value) + "-->"
            while temp is not self.last:
                temp = temp.next
                repr += str(temp.value) + "-->"
            # temp is self.last here, so we have reached at starting point.
            # add temp.last as reference
            repr += "Reached last node:" + str(temp.value) + ".Next = " + str(temp.next.value)
        else:
            print("List is empty")
            return

        print(repr)

    def addToBeg(self, value):
        node = Node(value)
        if self.last is None:
            self.last = node
            node.next = self.last
        else:
            first_node = self.last.next
            node.next = first_node
            self.last.next = node

    def addToEnd(self, value):
        node = Node(value)
        temp = self.last
        # make node point to first node, or last.next/temp.next
        node.next = temp.next
        # make the last node point node, node comes after temp
        temp.next = node
        # update last to new node
        self.last = node

    def addAtPos(self, value, pos_value):
        node = Node(value)
        # take first node
        temp = self.last.next
        # traverse till last node
        while temp is not self.last:
            if temp.value == pos_value:
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next

    def deleteAtBeg(self):
        # get last node
        temp = self.last
        # get first node
        node_to_delete = temp.next
        # make last node point to 2nd node
        self.last.next = node_to_delete.next

    def deleteAtEnd(self):
        # take first pointer
        temp = self.last.next

        # traverse to 2nd last node
        while temp.next is not self.last:
            temp = temp.next

        # temp is 2nd last node here, as loop condition is now temp.next=self.last
        # make 2nd node point to first node to maintain circular property
        temp.next = self.last.next
        # make last pointer point to this node
        # thus last node will be deleted
        self.last = temp

    def deleteAtPos(self, value):
        # take first node
        temp = self.last.next

        # traverse till last node
        while temp.next is not self.last:
            # delete temp.next. make temp (prev node) point to node after temp.next
            if temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next


if __name__ == "__main__":
    cll = CLL()
    cll.addToBeg(50)
    cll.addToBeg(53)
    cll.__repr__()

    cll.addToEnd(90)
    cll.__repr__()

    cll.addAtPos(80, 50)
    cll.addAtPos(100, 80)
    cll.addAtPos(90, 100)
    cll.addAtPos(32, 100)
    cll.addAtPos(75, 100)
    cll.__repr__()

    cll.deleteAtBeg()
    cll.__repr__()

    cll.deleteAtEnd()
    cll.__repr__()

    cll.deleteAtPos(75)
    cll.deleteAtPos(74)
    cll.__repr__()
