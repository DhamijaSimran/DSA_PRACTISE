# detect cycle in LL
# swap nodes of LL
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
        nodes = [Node(i) for i in range(1, 11)]
        self.head = nodes[0]
        for i in range(0, 9):
            nodes[i].next = nodes[i + 1]
        nodes[9].next = None

    def swapNodes(self, val1, val2):
        if val1 == val2:
            return

        temp = self.head
        node1 = None
        node2 = None
        prev1 = None
        prev2 = None
        current = None

        # find all nodes - node1,node2,prev1,prev2
        while temp is not None:
            if temp.value == val1:
                prev1 = current
                node1 = temp
            if temp.value == val2:
                prev2 = current
                node2 = temp
            current = temp
            temp = temp.next

        # set1 = [prev1, node1, next1]
        # data1 = [i.value if i else i for i in set1]
        # print(data1)
        #
        # set2 = [prev2, node2, next2]
        # data2 = [i.value if i else i for i in set2]
        # print(data2)

        # swap
        if node1 is node2:
            return
        if node1 is None or node2 is None:
            return

        if prev1 is not None:
            prev1.next = node2
        else:
            self.head = node2

        if prev2 is not None:
            prev2.next = node1
        else:
            self.head = node1

        temp = node1.next
        node1.next = node2.next
        node2.next = temp

    def swapNodesInPairs(self):

        prev = self.head
        current = self.head.next
        self.head = self.head.next

        if self.head is None or self.head.next is None:
            print("Pair of nodes not available to swap")
            return

        while current is not None:
            # save pointers
            nextNode = current.next

            # swap the nodes current and prev
            current.next = prev

            # we are on last pair of nodes, or one odd single node
            if nextNode is None:
                prev.next = nextNode
                break

            prev.next = nextNode.next

            # move to next pair
            prev = nextNode
            current = nextNode.next

    def rotateListByKNodes(self, k):

        # find 1st node of upto kth node, and find beginning of rest of nodes
        # traverse the list and maintain pointers to beginning of both groups
        # make end of 2nd group point to beginning of 1st group
        # make end of 1st group point to null
        # make head point to beginning of 2nd group

        temp = self.head
        len = 0

        # first k nodes
        k_beg = temp
        k_end = None

        # remaining nodes
        l_beg = None
        l_end = None

        while temp is not None:
            len += 1

            if len == k:
                k_end = temp
                l_beg = k_end.next

            # reached end of list
            if temp.next is None:
                l_end = temp

            # go to next node
            temp = temp.next

        # rotate
        if l_beg and l_end and k_end:
            self.head = l_beg
            l_end.next = k_beg
            k_end.next = None
        else:
            print("k not found")
            return

    # reversing a linked list in K groups
    # imagine traversing backwards from node k
    # we have to do above for each group of k nodes
    # eg 8->9->0->1->3->5->2 and k=3. traverse backwards from every 3rd node
    # result 0->9->8->5->3->1->2. if k=5 then
    # result 3->1->0->9->8->5->2
    def reverseLLInKgroups(self, head, k):

        if head == None:
            return

        temp=head
        count = 0

        # check if at least k number of nodes exist
        # to reverse
        while temp is not None:
            count+=1
            temp=temp.next

        if count<k:
            return head

        count = 0
        current = head
        prev = None
        next = None

        # reverse this group of k nodes
        # save next node. next node will be
        # first node when reversed, and prev will be
        # last node when reversed, in this group
        # reverse step: current.next=prev, prev=current, current=current.next
        while count < k and current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        # if first node in next k group is not None
        # there are more nodes to reverse.
        # head node in any k group will become last after reverse
        # so next of head node is first node in next k group
        # so pass next as head for next k group
        if next is not None:
            head.next = self.reverseLLInKgroups(next, k)

        # prev will be new head of k group after reverse
        # prev is last node of k group before reversal.
        # as calls to this function is recursive,
        # when next is None, (at end of LL), last k-groups
        # head is returned to the previous k-groups stack;
        # previous k-groups stack returns its head, and so on
        # till first k-groups stack returns prev, which is the
        # head of LL.
        return prev

    def concatenateLL(self, LL2):
        temp1 = self.head
        temp2 = LL2.head

        while temp1.next is not None:
            temp1 = temp1.next

        temp1.next = temp2

        print("Linked List concatenated")

    def splitLL(self, k, new_head):
        temp = new_head
        count = 0

        # get group of k nodes
        # 1st node is new_head, next k-1 nodes needed
        # temp may become none even when count<k-1
        while count < k - 1 and temp is not None:
            temp = temp.next
            count += 1

        # if nodes less than k, print remaining list
        # then return.
        if temp is None:
            # print this split list
            dummy = new_head
            str_rep = ""
            while dummy is not None:
                str_rep += str(dummy.value) + "-->"
                dummy = dummy.next
            str_rep += "None"
            print(str_rep)
            return

        # end of k group. store the next node before
        # making this node point to null
        next = temp.next
        temp.next = None

        # print this split list
        dummy = new_head
        str_rep = ""
        while dummy is not None:
            str_rep += str(dummy.value) + "-->"
            dummy = dummy.next
        str_rep += "None"
        print(str_rep)

        # move the new_head to remaining nodes
        # for next recursive call
        new_head = next

        if new_head is not None:
            self.splitLL(k, new_head)


if __name__ == "__main__":
    LL = LinkedList()
    LL.createLL()
    LL.__repr__()

    print("swapNodes(2, 8)")
    LL.swapNodes(2, 8)
    LL.__repr__()

    print("swapNodes(2, 10)")
    LL.swapNodes(2, 10)
    LL.__repr__()

    print("swapNodes(1, 8)")
    LL.swapNodes(1, 8)
    LL.__repr__()

    print("swapNodes(1, 10)")
    LL.swapNodes(1, 10)
    LL.__repr__()

    print("swapNodesInPairs()")
    LL.swapNodesInPairs()
    LL.__repr__()

    print("rotateListByKNodes(2)")
    LL.rotateListByKNodes(2)
    LL.__repr__()

    print("rotateListByKNodes(10)")
    LL.rotateListByKNodes(10)
    LL.__repr__()

    LL2 = LinkedList()
    LL2.createLL()
    print("concatenateLL")
    LL.concatenateLL(LL2)
    LL.__repr__()

    # print("splitLL(3)")
    # LL.splitLL(8, LL.head)

    print("reverseLLInKgroups(3)")
    LL.head = LL.reverseLLInKgroups(LL.head, 7)
    LL.__repr__()
