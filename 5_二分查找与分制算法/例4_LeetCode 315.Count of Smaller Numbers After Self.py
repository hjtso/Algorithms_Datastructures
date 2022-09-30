class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        n = len(nums)
        ans = [None]*n
        tmp = []
        for i in range(n-1, -1, -1):
            t = nums[i]
            pos = bisect.bisect_left(tmp, t)
            ans[i] = pos
            tmp.insert(pos, t)

        return ans

# https://blog.csdn.net/PKU_Jade/article/details/77932357