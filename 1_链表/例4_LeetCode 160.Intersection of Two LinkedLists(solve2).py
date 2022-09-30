# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list_A_len = self.getListLength(headA)
        list_B_len = self.getListLength(headB)
        if list_A_len > list_B_len:
            headA = self.forwardLongList(list_A_len, list_B_len, headA)
        else:
            headB = self.forwardLongList(list_B_len, list_A_len, headB)
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def getListLength(self, head) -> int:
        len_node = 0
        while head:
            len_node += 1
            head = head.next
        return len_node

    def forwardLongList(self, long_len, short_len, head) -> ListNode:
        delta = long_len - short_len
        while head and delta:
            head = head.next
            delta -= 1
        return head