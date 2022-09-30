class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        all_set = 1 << len(nums)
        for i in range(all_set):
            item = []
            for j in range(len(nums)):
                if i & (1 << j):
                    item.append(nums[j])
            result.append(item)
        return result
