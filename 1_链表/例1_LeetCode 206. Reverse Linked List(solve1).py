# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next

        return new_head
