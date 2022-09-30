class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.lowwer_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def lowwer_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# https://blog.csdn.net/fuxuemingzhu/article/details/83273084