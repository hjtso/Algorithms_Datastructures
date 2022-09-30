from heapq import *


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1

        h = []
        for i in range(len(nums)):
            if len(h) < k:
                heappush(h, nums[i])
            else:
                if h[0] < nums[i]:
                    heappop(h)
                    heappush(h, nums[i])

        return h[0]

# https://www.cnblogs.com/lightwindy/p/8514845.html