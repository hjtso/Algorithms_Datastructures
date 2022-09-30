# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_set = set()
        while headA:
            node_set.add(headA)
            headA = headA.next
        while headB:
            if headB in node_set:
                return headB
            headB = headB.next
        return None