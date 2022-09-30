class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class Link():
    def __init__(self):
        self._head = None
        # self._tail = None

    # 向链表的头部插入一个节点（栈）
    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def travel(self):
        node = self._head
        while node:
            print(node.item)
            node = node.next

    def isEmpty(self):
        return False if self._head else True

    def size(self):
        count = 0
        node = self._head
        while node:
            count = count + 1
            node = node.next
        return count

    # 向链表尾部添加一个Node（队列）
    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self._head = node
        # else:
        #     self._tail.next = node
        # self._tail = node
        else:
            pre = None  # 用于记录最后一个节点
            cur = self._head
            while cur:
                pre = cur
                cur = cur.next
            pre.next = node

        # 此操作不可行，因为最后一个cur为空，需要在前面的pre指向新节点
        # node = Node(item)
        # if self.isEmpty():
        #     self._head = node
        # else:
        #     cur = self._head
        #     while cur:
        #         cur = cur.next
        #     cur.next = node

    # search指定item在链表中哪个位置,返回一个位置list，如果没有，则为空列表
    def search(self, item):
        indexs = []
        count = 0
        node = self._head
        while node:
            if item == node.item:
                indexs.append(count)
            count = count + 1
            node = node.next
        if len(indexs) == 0:
            print(False)
            return None
        else:
            print(True)
            return indexs

    def insert(self, index, item):
        ori_sizw = self.size()
        if index > ori_sizw:
            print("index out of link range!")
        else:
            if index == 0 or ori_sizw == 0:
                self.add(item)
            elif index == ori_sizw:
                self.append(item)
            else:
                node = Node(item)
                pre = self._head
                for i in range(1, index):
                    pre = pre.next()

                node.next = pre.next
                pre.next = node

    def remove_index(self, index):
        if index == 0:
            self._head = self._head.next
        else:
            pre = None
            cur = self._head
            for i in range(index):
                pre = cur
                cur = cur.next
            pre.next = cur.next

    def remove_item(self, item):
        indexs = self.search(item)
        if len(indexs) == None:
            print('item not in link')
            return False
        else:
            count = 0
            for index in indexs:
                index = index - count
                self.remove_index(index)
                count += 1

    def reverse(self):
        pre = None
        cur = self._head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        self._head = pre

        # new_head = None
        # head = self._head
        # while head:
        #     next = head.next
        #     head.next = new_head
        #     new_head = head
        #     head = next
        # self._head = new_head

# https://blog.csdn.net/weixin_43718675/article/details/105553490
link = Link()
link.append(4)
link.add(3)
link.add(5)
link.append(8)
link.travel()


# link.add(1)
# link.add(2)
# link.add(3)
# link.add(4)
# link.travel()
# link.reverse()
# link.travel()


class LinkNode():
    def __init__(self, item):
        self.item = item
        self.head = None
        self.next = None


class DoubleLink():
    def __init__(self):
        self._head = None

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        if self.size() == 0:
            self.add(item)
        else:
            node = LinkNode(item)
            pre = None
            cur = self._head
            while cur:
                pre = cur
                cur = cur.next
            pre.next = node
            node.head = pre

    def insert(self, index, item):
        ori_size = self.size()
        if ori_size == 0 or index == 0:
            self.add(item)
        elif ori_size == index:
            self.append(item)
        else:
            node = Node(item)

            pre = None
            cur = self._head
            for i in range(0, index):
                pre = cur
                cur = cur.next

            cur.head = node
            node.next = cur

            node.head = pre
            pre.next = node

    def travel(self):
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def size(self):
        count = 0
        cur = self._head
        while cur:
            cur = cur.next
            count += 1
        return count

# doublelink = DoubleLink()
# doublelink.append(1)
# doublelink.append(2)
# doublelink.append(3)
# doublelink.append(4)
# doublelink.insert(2,5)
# doublelink.travel()





