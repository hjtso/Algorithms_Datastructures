import math

# 链表实现
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, item):
        node = Node(item)

        if self.root == None:
            self.root = node
        else:
            List = [self.root]
            while List:
                q = List.pop(0)
                if q.left == None:
                    q.left = node
                    break
                else:
                    List.append(q.left)
                if q.right == None:
                    q.right = node
                    break
                else:
                    List.append(q.right)

    def BFS_travel(self):
        # sum_dict = {}
        # index = 0
        List = [self.root]
        while List:
            q = List.pop(0)
            print(q.item)
            # try:
            #     sum_dict[int(math.log2(index+1))] += q.item
            # except KeyError:
            #     sum_dict[int(math.log2(index+1))] = q.item
            if q.left != None:
                List.append(q.left)
            if q.right != None:
                List.append(q.right)
        #     index += 1
        # print(sum_dict)

    def DFS_Forward(self, root):
        if root != None:
            print(root.item)
            self.DFS_Forward(root.left)
            self.DFS_Forward(root.right)

    def DFS_Middle(self, root):
        if root != None:
            self.DFS_Forward(root.left)
            print(root.item)
            self.DFS_Forward(root.right)

    def DFS_Backward(self, root):
        if root != None:
            self.DFS_Forward(root.left)
            self.DFS_Forward(root.right)
            print(root.item)


tree = Tree()
tree.add_node(1)
tree.add_node(2)
tree.add_node(3)
tree.add_node(4)
tree.add_node(5)
tree.add_node(6)
tree.add_node(7)
tree.add_node(8)

tree.BFS_travel()


# tree.DFS_Forward(tree.root)
# tree.DFS_Middle(tree.root)
# tree.DFS_Backward(tree.root)


# 排序二叉树
class SortedTree():
    def __init__(self):
        self.root = Node

    # 添加节点时：大于根节点的在右子节点，大小等于根节点的在左子节点
    def add_node(self, item):
        node = Node(item)
        # cur = self.root
        if self.root == None:
            self.root = node
        else:
            cur = self.root
            while True:
                if item > cur.item:
                    if cur.right == None:
                        cur.right = node
                        break
                    else:
                        cur = cur.right
                else:
                    if cur.left == None:
                        cur.left = node
                        break
                    else:
                        cur = cur.left

    # 遍历树,按照添加节点顺序输出节点数值: 按层从左到右遍历 --- 广度优先遍历
    def BFS_travel(self):
        List = [self.root]
        while List:
            q = List.pop(0)
            print(q.item)
            if q.left != None:
                List.append(q.left)
            if q.right != None:
                List.append(q.right)

    # 遍历树：深度优先算法：前序遍历 --根左右
    def DFS_Forward(self, root):
        if root != None:
            print(root.item)
            self.DFS_Forward(root.left)
            self.DFS_Forward(root.right)

    # 深度优先算法：中序遍历 --左根右
    def DFS_Middle(self, root):
        if root != None:
            self.DFS_Middle(root.left)
            print(root.item)
            self.DFS_Middle(root.right)

    # 深度优先算法：后序遍历 -- 左右根
    def DFS_Backward(self, root):
        if root != None:
            self.DFS_Backward(root.left)
            self.DFS_Backward(root.right)
            print(root.item)


sortedTree = SortedTree()
sortedTree.add_node(3)
sortedTree.add_node(8)
sortedTree.add_node(5)
sortedTree.add_node(7)
sortedTree.add_node(6)
sortedTree.add_node(2)
sortedTree.add_node(9)
sortedTree.add_node(4)
sortedTree.add_node(1)
print('DFS_Forward:')
sortedTree.DFS_Forward(sortedTree.root)
print('DFS_Middle:')
sortedTree.DFS_Middle(sortedTree.root)
print('DFS_Backward:')
sortedTree.DFS_Backward(sortedTree.root)






# 数组实现
def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)
insert_left(l, 11)
print(r)
print(get_right_child(get_right_child(r)))
