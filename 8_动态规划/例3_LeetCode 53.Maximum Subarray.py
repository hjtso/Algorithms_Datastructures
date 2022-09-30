class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [0]*size
        dp[0] = nums[0]
        max_res = dp[0]
        for i in range(1, size):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if max_res < dp[i]:
                max_res = dp[i]
        return max_res