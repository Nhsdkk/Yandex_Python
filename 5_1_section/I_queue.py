class Item:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def insert(self, value):
        if self.next is not None:
            item = Item(value)
            item.next = self.next
            item.prev = self
            self.next.prev = item
            self.next = item
            return

        self.prev.insert(value)

    def pop(self):
        if self.prev is not None:
            value = self.value
            self.next.prev = self.prev
            self.prev.next = self.next
            return value

        return self.next.pop()


class Queue:
    def __init__(self):
        self.front = Item(None)
        self.back = Item(None)
        self.front.next = self.back
        self.back.prev = self.front
        self.size = 0

    def push(self, value):
        self.size += 1
        self.back.insert(value)

    def pop(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        self.size -= 1
        return self.front.pop()

    def is_empty(self):
        return self.size == 0
