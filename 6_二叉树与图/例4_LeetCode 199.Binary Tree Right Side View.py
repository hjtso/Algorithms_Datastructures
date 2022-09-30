# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
# collections.deque()库
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

# https://blog.csdn.net/fuxuemingzhu/article/details/79557632

# queue.Queue()库
# class Solution(object):
#     def rightSideView(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root is None:
#             return []
#         res = self.BFS_travle(root)
#         fin = []
#         for value in res.values():
#             fin.append(value[-1])
#         return fin
#
#     def BFS_travle(self, root):
#         from queue import Queue
#         queue = Queue()
#         queue.put((0, root))
#         sum_dict = {}
#         while not queue.empty():
#             (level, node) = queue.get()
#             try:
#                 sum_dict[level].append(node.val)
#             except KeyError:
#                 sum_dict[level] = []
#                 sum_dict[level].append(node.val)
#
#             if node.left:
#                 queue.put((level + 1, node.left))
#             if node.right:
#                 queue.put((level + 1, node.right))
#
#         return sum_dict



# 只适用于完全二叉树
# class Solution(object):
#     def rightSideView(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root is None:
#             return []
#         res = self.BFS_travle(root)
#         fin = []
#         for value in res.values():
#             fin.append(value[-1])
#         return fin
#
#     def BFS_travle(self, root):
#         sum_dict = {}
#         index = 0
#         List = [root]
#         while List:
#             q = List.pop(0)
#             try:
#                 sum_dict[int(math.log2(index+1))].append(q.val)
#             except KeyError:
#                 sum_dict[int(math.log2(index+1))] = []
#                 sum_dict[int(math.log2(index+1))].append(q.val)
#             if q.left != None:
#                 List.append(q.left)
#             if q.right != None:
#                 List.append(q.right)
#             index += 1
#         print(sum_dict)
#         return sum_dict