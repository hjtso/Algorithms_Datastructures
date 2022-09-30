# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        meet = None
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if fast == slow:
                meet = fast
                break

        if meet is None:
            return None

        while head and meet:
            if head == meet:
                return head
            head = head.next
            meet = meet.next

        return None