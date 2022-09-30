class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]: # 主函数，准备递归物料、递归函数入口
        self.res = []   # 答案记录器
        self.n = n      # 方便会用到的子函数
        tmp = [None for _ in range(self.n)]   # 递归复用数组，用一维数组记录Queen位置，数组的index就是row，index对应的元素就是col
        self.backtrace(tmp, row=0)
        return self.return_result()

    def backtrace(self, tmp, row):
        if row == self.n:  # 如果已经判断完全部的行了，就返回并记录吧
            self.res.append(tmp[:])   # 这里必须是tmp的切片，因为python切片是浅拷贝，浅拷贝的结果不会在后续递归中被修改掉
            return         # 这里必须有一个return，因为当row == self.n成立时，这条递归之路即该完美结束
        col = 0   # 每一行的循环判断，都从0位置开始
        while col < self.n:
            if self.is_valid(tmp, row, col):  # 判断当前位置是否可放Queen
                tmp[row] = col             # 若可以，则记录于tmp
                self.backtrace(tmp, row + 1)   # 然后开启下一行的递归判断(row+1)
            col += 1      # 不论是否成立，都应将col的位置步进(col+1)
        return  # 这里必须有一个return，因为当while循环跳出，说明本行所有col都不能放Queen，应发生回溯，目前的递归之路应提前结束

    def is_valid(self, tmp, row, col):
        for i, j in enumerate(tmp):
            # 在判断Queen是否可放置的时候，只有当前行之前的Queen值得被考虑。由于tmp是复用的，所以当前row及其之后的row都有可能已有无用记录
            if i == row:
                break
            if j == col or row - i == abs(col - j):  # 两个不可放Queen条件：1.在同列；2.在**左、右**两侧对角线。
                return False
        return True   # 全部经历过考验，则可以放置

    def return_result(self):   # 将结果转换成LeetCode要求的样子
        saver = []
        for arr in self.res:
            solve = []
            for pos in arr:
                line = ["."] * self.n
                line[pos] = "Q"
                solve.append(''.join(line))
            saver.append(solve)
        return saver


# https://blog.csdn.net/weixin_41712499/article/details/109692357
