class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
        self.counter += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.counter -= 1
                return
            prev = current
            current = current.next


nums = SingleLinkedList()
nums.append(1)
nums.append(1)
nums.append(3)
for i in nums.iter():
    print(i)

nums.delete(1)

for i in nums.iter():
    print(i)
