# 数组实现
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def travel(self):
        for i in self.items:
            print(i)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.travel()





# 链表实现
class Node():
    def __init__(self, e):
        self.element = e
        self.next = None


class Queue():
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def enqueue(self, e):
        newest = Node(e)

        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self._size += 1

    def deuqueue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')

        elementToReturn = self.head.element
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None

        return elementToReturn

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.head.element

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size













