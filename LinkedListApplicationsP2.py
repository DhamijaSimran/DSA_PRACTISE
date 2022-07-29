import copy
import random


class Node1:
    def __init__(self, coeff=0, exp=0):
        self.next = None
        self.coeff = coeff
        self.exp = exp


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

    def mergeLL(self, LL2):
        head1 = self.head
        head2 = LL2.head
        LL3 = LinkedList()

        while head1 is not None and head2 is not None:
            # print(head1.value)
            # print(head2.value)
            if head1.value < head2.value:
                LL3.insert_node(LL3, copy.deepcopy(head1))
                head1 = head1.next
            elif head2.value < head1.value:
                LL3.insert_node(LL3, copy.deepcopy(head2))
                head2 = head2.next
            else:
                LL3.insert_node(LL3, copy.deepcopy(head2))
                head1 = head1.next
                head2 = head2.next

        while head1 is not None:
            # print(head1.value)
            LL3.insert_node(LL3, copy.deepcopy(head1))
            head1 = head1.next

        while head2 is not None:
            # print(head2.value)
            LL3.insert_node(LL3, copy.deepcopy(head2))
            head2 = head2.next

        LL3.__repr__()

    # insert node in ascending order
    def insert_node(self, LL3, node):
        # print(node.value)
        # insert node at beginning if list is empty or if this node
        # is smaller than head node
        if LL3.head is None or node.value < LL3.head.value:
            node.next = LL3.head
            LL3.head = node
        else:
            # find position where temp.next is the first bigger node than this node
            # loop traverses till temp.next.value becomes greater than node.value
            # then temp is the node just smaller than this node, and temp.next is the
            # node just bigger than this node
            temp = LL3.head

            while temp.next is not None and temp.next.value <= node.value:
                temp = temp.next

            node.next = temp.next
            temp.next = node

        # LL3.__repr__()

    def insert_polynode(self, poly_LL, node):
        temp = poly_LL.head

        if poly_LL.head is None or poly_LL.head.exp > node.exp:
            node.next = poly_LL.head
            poly_LL.head = node
        else:
            while temp.next is not None and temp.next.exp <= node.exp:
                temp = temp.next

            node.next = temp.next
            temp.next = node

    def createLLPolynomial(self):
        nodes = [Node1(random.randint(1, 5), random.randint(1, 5)) for i in range(1, 7)]
        self.head = nodes[0]
        for i in range(0, 5):
            nodes[i].next = nodes[i + 1]
        nodes[5].next = None

        repr = ""
        len = 0
        temp = self.head
        while temp is not None:
            repr += str(temp.coeff) + "x^" + str(temp.exp) + "-->"
            len += 1
            temp = temp.next
        repr += "None"
        print(repr)

    # a polynomial such as 5x^3 + 7x^2 + 2
    # can be represented in terms of coeffecient and
    # exponent of x. store both in LL fields
    # eg node.coeff = 5 and node.exp = 3
    # thus LL representation of above polynomial
    # is node0.coeff = 5 node0.exp = 3 node0.next=node1
    #    node1.coeff = 7 node1.exp = 2 node1.next=node2
    #    node2.coeff = 2 node2.exp = 0 node2.next=None

    # arithmatic of polynomials would mean performing ops on coeffs
    # and exponents, and storing results in 3rd LL

    def multiplyPolynomial(self, LL2):
        head1 = self.head
        head2 = LL2.head
        polyLL3 = LinkedList()

        while head1.next is not None and head2.next is not None:
            if head1.exp == head2.exp:
                # print("head1 " + str(head1.coeff) + "x^" + str(head1.exp))
                # print("head2 " + str(head2.coeff) + "x^" + str(head2.exp))
                Node = Node1(head1.coeff * head2.coeff, head1.exp)
                # print("New Node " + str(Node.coeff) + "x^" + str(Node.exp))
                polyLL3.insert_polynode(polyLL3, Node)
                head1 = head1.next
                head2 = head2.next
            elif head1.exp < head2.exp:
                polyLL3.insert_polynode(polyLL3, copy.deepcopy(head1))
                head1 = head1.next
            else:
                polyLL3.insert_polynode(polyLL3, copy.deepcopy(head2))
                head2 = head2.next

        while head1.next is not None:
            polyLL3.insert_polynode(polyLL3, copy.deepcopy(head1))
            head1 = head1.next

        while head2.next is not None:
            polyLL3.insert_polynode(polyLL3, copy.deepcopy(head2))
            head2 = head2.next

        repr = ""
        len = 0
        temp = copy.deepcopy(polyLL3.head)
        while temp is not None:
            repr += str(temp.coeff) + "x^" + str(temp.exp) + "-->"
            len += 1
            temp = temp.next
        repr += "None"
        print(repr)

        polyLL3.mergeMultPolynomialLL()

    # multiply similar nodes (with same exponent)
    def mergeMultPolynomialLL(self):
        # get copy of this linked list
        polyLL4 = copy.deepcopy(self)
        temp = polyLL4.head
        # keep track of prev pointer. all merging done in polyLL4
        prev = None

        while temp is not None and temp.next is not None:
            # condition to merge 2 nodes
            if temp.exp == temp.next.exp:
                # get new node that is the combination of 2 nodes to be merged
                Node = Node1(temp.coeff + temp.next.coeff, temp.exp)

                # we have to insert this node in place of the 2 nodes we have merged/combined
                # temp and temp.next are merged. Node will replace temp.next
                # thus node.next will point to temp.next.next
                # and the node previous to this new merged node, will point to this new merged Node
                # the previous node is NOT temp, it is the previous merged/existing node
                # temp and temp.next are merged, so temp is no more, and Node is replacing temp.next
                # thus prev.next = Node
                # and now we update temp to Node, so that in next iteration,
                # Node and Node.next are compared.
                # is this node supposed to be the head node? check with head
                if temp.coeff == polyLL4.head.coeff and temp.exp == polyLL4.head.exp:
                    prev = polyLL4.head
                    polyLL4.head = Node
                else:
                    # print("else exp " + str(temp.exp) + " " + str(temp.coeff) + " " + str(temp.next.coeff))
                    prev.next = Node
                Node.next = temp.next.next
                temp = Node
            else:
                prev = temp
                temp = temp.next

        temp = copy.deepcopy(polyLL4.head)
        repr = ""
        while temp is not None:
            repr += str(temp.coeff) + "x^" + str(temp.exp) + "-->"
            temp = temp.next
        repr += "None"
        print(repr)

    def addPolynomials(self, polyLL5):
        head1 = self.head
        head2 = polyLL5.head

        polyLL6 = LinkedList()

        while head1 is not None and head2 is not None:
            if head1.exp == head2.exp:
                node = Node1(head1.coeff + head2.coeff, head1.exp)
                polyLL6.insert_polynode(polyLL6, node)
                head1 = head1.next
                head2 = head2.next

            elif head1.exp < head2.exp:
                polyLL6.insert_polynode(polyLL6, copy.deepcopy(head1))
                head1 = head1.next

            else:
                polyLL6.insert_polynode(polyLL6, copy.deepcopy(head2))
                head2 = head2.next

        repr = ""
        len = 0
        temp = copy.deepcopy(polyLL6.head)
        while temp is not None:
            repr += str(temp.coeff) + "x^" + str(temp.exp) + "-->"
            len += 1
            temp = temp.next
        repr += "None"
        print(repr)
        polyLL6.mergeMultPolynomialLL()


if __name__ == "__main__":
    LL = LinkedList()
    LL.createLL()
    LL.__repr__()

    LL2 = LinkedList()
    LL2.createLL()
    LL2.__repr__()

    print("Merging LL")
    LL.mergeLL(LL2)
    # LL.createLLPolynomial()

    print("Creating polynomials for multiplication")
    polyLL = LinkedList()
    polyLL.createLLPolynomial()
    polyLL1 = LinkedList()
    polyLL1.createLLPolynomial()

    print("Multiplying polynomials")
    polyLL.multiplyPolynomial(polyLL1)

    print("Creating polynomials for addition")
    polyLL4 = LinkedList()
    polyLL4.createLLPolynomial()
    polyLL5 = LinkedList()
    polyLL5.createLLPolynomial()

    print("Adding polynomials")
    polyLL4.addPolynomials(polyLL5)
