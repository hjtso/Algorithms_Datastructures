# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.afterOrder(root)
        return root

    def afterOrder(self, cur):
        if not cur: return
        self.afterOrder(cur.right)
        self.sum += cur.val
        cur.val = self.sum
        self.afterOrder(cur.left)

# https://blog.csdn.net/fuxuemingzhu/article/details/79132336