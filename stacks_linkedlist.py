""" push and pop will happen in beginning of linked list. here we can just do operation and not traverse the
full list, as we would have to if ops done at end of ll.
top points to beginning of LL."""

class Node():
    def __init__(self, ele):
        self.data = ele
        self.next = None

def traverseLL():
    global top
    pointer = top
    rep = ""
    while pointer is not None:
        rep += (str(pointer.data) + "->")
        pointer = pointer.next
    rep += "None"
    print(rep)

def check_underflow():
    global top
    if top is None:
        return True
    return False


def check_overflow():
    global top,max_size
    count = 0
    pointer = top
    print("Traversing the list before push for overflow check.")
    while pointer is not None:
        print("Element at {} position is {}".format(count,pointer.data))
        pointer = pointer.next
        count += 1
    print("Current size of stack ",str(count))
    if count>max_size-1:
        return True
    return False

def push(eles):
    global top
    for i in eles:
        if not check_overflow():
            print("No overflow. Inserting",i)
            new_node = Node(i)
            new_node.next = top
            top = new_node
        else:
            print("Overflow has occurred. Aborting")

def pop(count):
    global top
    for i in range(count):
        if not check_underflow():
            print("Popping element",top.data)
            top = top.next
            traverseLL()
        else:
            print("Underflow has occurred. Aborting")
            exit(1)

if __name__ == "__main__":
    max_size = 5
    top = None
    if top is None:
        print("push([50, 8, 48, 93, 0, 88])")
        push([50, 8, 48, 93, 0, 88])
    traverseLL()
    print("pop(6)")
    pop(6)
    traverseLL()

