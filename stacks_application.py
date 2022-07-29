def check_valid_parentheses(s):
    brackets = {"(": ")", "{": "}", "[": "]"}

    stack = []

    for i in s:

        # append only opening brackets
        if i in brackets.keys():
            stack.append(i)

        # something else except opening brackets in str
        # should be a closing bracket only, no other chars
        # check if length of stack is 0 in case first char is closing bracket
        # else check if its opening bracket is in stack
        # by popping stack. if mismatch then return false and end loop here
        elif len(stack) == 0 or brackets[stack.pop()] != i:
            return False

    # iterated through string. stack should be empty here, otherwise an extra opening
    # bracket is in stack, which is mismatch.
    return len(stack) == 0


def reverse_string(str):
    stack = [None] * 20
    top = 0
    max_size = 20

    # push
    for i in str:
        if top < max_size:
            stack[top] = i
            top += 1
        else:
            print("Overflow, aborting")

    # pop
    while top >= 0:
        print(stack[top])
        top -= 1

if __name__ == "__main__":
    print(check_valid_parentheses("[])*]{"))
    print(check_valid_parentheses("[]()*[]{}"))
    print(check_valid_parentheses("[]()[]{}"))
    reverse_string("HELLO")
