''' if stack has ele 0 in it, assume it to be empty.'''
stack = [0] * 10
top = 0
max_size = 10
min_size = 0


def push(arr):
    global stack, top
    for i in arr:
        if not check_overflow():
            stack[top] = i
            print("element at {} index is {}".format(top, i))
            top += 1
        else:
            '''top is an index and has overflowed. make it point to the topmost index instead of size
                by doing -1'''
            top -= 1
            print("Overflow. Abort")


def pop(count):
    global stack, top
    for i in range(count):
        if not check_underflow():
            print("popped element {} at {}".format(stack[top],top))
            stack[top] = 0
            top -= 1
        else:
            '''top is an index and has overflowed. make it point to the topmost index instead of size
                            by doing +1'''
            top += 1
            print("Underflow. Abort")

''' top references index in array, whereas max_size and min_size refer sizes. 
    max_size will always be 1 more than top as index starts from 0
    min_size is 0 of any array, which is also the lowest index of any array
    so comparison can be made directly for check_undeflow 
'''

def check_underflow():
    global top, min_size
    if top < min_size:
        return True
    return False


def check_overflow():
    global top, max_size
    if top > max_size-1:
        return True
    return False


if __name__ == "__main__":
    print("stack before program run:")
    print(stack)
    print("push([5,6,7,3,2,1,13,90,21,55])")
    push([5, 6, 7, 3, 2, 1, 13, 90, 21, 55])
    push([83])
    print("pop(11)")
    pop(11)
    print("stack after program run:")
    print(stack)
