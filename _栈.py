# 数组实现
class Stack():
    def __init__(self):
        self.items = []

    def enstack(self, item):
        self.items.append(item)

    def destack(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def travel(self):
        lenth = len(self.items)
        for i in range(lenth-1, -1, -1):
            print(self.items[i])


stack = Stack()
stack.enstack(1)
stack.enstack(2)
stack.enstack(3)
stack.enstack(4)
stack.destack()
stack.travel()




# 链表实现
class Node():
    def __init__(self,e):
        self.element = e
        self.next = None


class Stack():
    def __init__(self):
        self._size = 0
        self.head = None

    def push(self, e):
        newest = Node(e)
        newest.next = self.head
        self.head = newest
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        elementToReturn = self.head.element
        self.head = self.head.next
        self._size -= 1

        return elementToReturn

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.head.element

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size