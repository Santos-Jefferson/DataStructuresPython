class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubledLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:  # if list is empty
            # Both head and tail will be the same, the new_node
            self.head = new_node
            self.tail = self.head
        else:  # if list is not empty
            # The new_node previous will be the current last item/element
            new_node.prev = self.tail
            # Then the last item.next has to be the new_node
            self.tail.next = new_node
            # Then the last item has to be the new_node
            self.tail = new_node
            # Increment the size/counter of the list
            self.counter += 1

    def delete(self, data):
        # Start from the first element
        current = self.head
        # A flag if is deleted or not
        node_deleted = False
        if current is None:  # If list is empty
            node_deleted = False  # keeps it False
        elif current.data == data:  # if item is the first element
            # the first node now will be the next (second node)
            self.head = current.next
            # As it will be the first node, it doesn't have a previous one
            self.head.prev = None
            # The flag is set to True
            node_deleted = True
        elif self.tail.data == data:  # if item is the last element
            # the last node now will be the previous node
            self.tail = self.tail.prev
            # as it will be the last one, it doesn't have a next one
            self.tail.next = None
            # The flag is set to True
            node_deleted = True
        else:  # if the node to be deleted is in the middle of the list:
            while current:
                if current.data == data:
                    # the next in the previous node needs to be the next of the current one
                    current.prev.next = current.next
                    # the previous in the next node needs to be the previous of the current one
                    current.next.prev = current.prev
                    # The flag is set to True
                    node_deleted = True
                current = current.next

        if node_deleted:
            # if it is True, decrement the counter
            self.counter -= 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
        return False


nums = DoubledLinkedList()
nums.append(1)
nums.append(2)
nums.append(3)
for i in nums.iter():
    print(i)

nums.delete(2)
for i in nums.iter():
    print(i)
