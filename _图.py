# 图的深度优先和广度优先遍历
def DFS(graph, s):  # 深度优先遍历,基于栈
    stack = []  # 建立栈
    stack.append(s)
    data = []  # 记录已经遍历过的点
    data.append(s)
    while stack:
        n = stack.pop()  # 取出栈中最后一个元素并删掉
        nodes = graph[n]
        for i in nodes[::-1]:  # 栈先进后出
            if i not in data:
                stack.append(i)
                data.append(i)
        print(n)


def BFS(graph, q):  # 广度优先遍历,基于队列
    queue = []  # 建立队列
    queue.append(q)
    data = []  # 记录已经遍历过的点
    data.append(q)
    while queue:
        n = queue.pop(0)  # 队列先进先出
        nodes = graph[n]
        for j in nodes:
            if j not in data:
                queue.append(j)
                data.append(j)
        print(n)


if __name__ == '__main__':
    graph = {
        '1': ['2', '3'],
        '2': ['4', '5'],
        '3': ['6', '7'],
        '4': ['8'],
        '5': ['8'],
        '6': ['7'],
        '7': [],
        '8': [],
    }
    print("深度优先遍历:")
    DFS(graph, '1')  # 结果为1,2,4,8,5,3,6,7
    print("广度优先遍历:")
    BFS(graph, '1')  # 结果为1,2,3,4,5,6,7,8

# https://pythontechworld.com/article/detail/sG3csp3p99LB
