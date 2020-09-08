class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:  # if stack is not empty
            # next node has to be the current top
            node.next = self.top
            # and now the top will be the node instantiated here
            self.top = node
        else:  # if stack is empty
            # the top has to be the node itself
            self.top = node
        # increment the size of the stack
        self.size += 1

    def pop(self):
        if self.top:  # of stack is not empty
            # data gets the current top value
            data = self.top.data
            # decrease the size of the stack
            self.size -= 1
            if self.top.next:  # if stack has a second node below
                # top has to be the next onto the stack (second node)
                self.top = self.top.next
            else:  # if stack has only 1 node
                # top will have nothing (None)
                self.top = None
            # return the data removed
            return data
        else:  # if stack is empty
            return None

    def peek(self):
        if self.top:  # if stack is not empty
            return self.top.data
        else:  # if stack is empty
            return None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)

poptest = stack.pop()
print(poptest)
poptest = stack.pop()
print(poptest)
poptest = stack.pop()
print(poptest)
