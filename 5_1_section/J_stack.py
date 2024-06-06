class Item:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def insert(self, value):
        if self.next is None:
            self.next = Item(value)
            self.next.prev = self
            return

        self.next.insert(value)

    def pop(self):
        if self.next is None:
            self.prev.next = None
            return self.value

        return self.next.pop()


class Stack:
    def __init__(self):
        self.front = Item(None)
        self.size = 0

    def push(self, item):
        self.size += 1
        self.front.insert(item)

    def pop(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        self.size -= 1
        return self.front.pop()

    def is_empty(self):
        return self.size == 0
