# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node_map = dict()

        prt = head
        while prt:
            node_map[prt] = Node(prt.val)
            prt = prt.next

        # 设置尾结点
        node_map[None] = None

        prt = head
        while prt:
            node_map[prt].next = node_map[prt.next]
            node_map[prt].random = node_map[prt.random]
            prt = prt.next

        return node_map[head]

# https://blog.csdn.net/alicelmx/article/details/83152017