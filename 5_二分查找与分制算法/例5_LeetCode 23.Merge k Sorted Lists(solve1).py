# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappop, heapify

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node_vec = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                node_vec.append(head)
                head = head.next

        if len(node_vec) == 0:
            return None

        for i in range(1,len(node_vec)):
            node_vec[i-1].next = node_vec[i]
        node_vec[len(node_vec)-1].next = None

        print(node_vec[0])
        node_vec = self.sortListNode(node_vec[0])
        print(node_vec)

        return node_vec

    def sortListNode(self, head):
        if not head or not head.next:
            return head

        temp = head
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next

        node_list.sort()
        head = temp
        i = 0
        while head:
            head.val = node_list[i]
            head = head.next
            i += 1

        return temp
