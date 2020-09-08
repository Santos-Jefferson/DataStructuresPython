class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        # Always insert items at index 0
        self.items.insert(0, data)
        # increment the size of the queue by 1
        self.size += 1

    def dequeue(self):
        # delete the topmost item from the queue
        data = self.items.pop()
        # decrement by 1
        self.size -= 1
        return data


class TwoStacksQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        # normal append to a list
        self.inbound_stack.append(data)

    def dequeue(self):
        # if outbound_stack is empty
        if not self.outbound_stack:
            # Transfer all items from inbound to outbound
            while self.inbound_stack:
                # append the topmost (.pop()) to the first one
                self.outbound_stack.append(self.inbound_stack.pop())
        # if outbound_stack is NOT empty, .pop() the topmost (first ones inserted)
        return self.outbound_stack.pop()


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = None(data, None, None)
        if self.head is None:  # if queue is empty
            # Head and Tail will be the new_node
            self.head = new_node
            self.tail = self.head
        else:  # if queue is not empty
            # previous node of new_node has to be the current last element
            new_node.prev = self.tail
            # the next of last node has to be new_node
            self.tail.next = new_node
            # and last element has to be the new node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        # Get the current first element
        current = self.head
        if self.count == 1:  # if queue has only 1 element
            # decrement by 1
            self.count -= 1
            # set head and tail to None
            self.head = None
            self.tail = None
        elif self.count > 1:  # if queue has 2 or more elements
            # the first has to be the next
            self.head = self.head.next
            # The previous of the first to None
            self.head.prev = None
            # Decrement by 1
            self.count -= 1
