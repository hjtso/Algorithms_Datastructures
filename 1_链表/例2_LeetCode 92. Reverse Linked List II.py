# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        change_len = n - m + 1
        pre_head = None
        result = head
        m-=1
        while head and m:
            pre_head = head
            head = head.next
            m-=1
        modify_list_tail = head

        new_head = None
        while head and change_len:
            next = head.next
            head.next = new_head
            new_head = head
            head = next
            change_len -= 1
        modify_list_tail.next = head

        if pre_head:
            pre_head.next = new_head
        else:
            result = new_head

        return result


# class Solution(object):
#     def reverseBetween(self, head, m, n):
#         """
#         :type head: ListNode
#         :type m: int
#         :type n: int
#         :rtype: ListNode
#         """
#         count = 1
#         root = ListNode(0)
#         root.next = head
#         pre = root
#         while pre.next and count < m:
#             pre = pre.next
#             count += 1
#         if count < m:
#             return head
#         mNode = pre.next
#         curr = mNode.next
#         while curr and count < n:
#             next = curr.next
#             curr.next = pre.next
#             pre.next = curr
#             mNode.next = next
#             curr = next
#             count += 1
#         return root.next

# https://blog.csdn.net/fuxuemingzhu/article/details/80794665