class Solution(object):
    def subCountSmaller(self, start_idx, nums):
        if not nums:
            return [], []
        if len(nums) == 1:
            return [0], nums

        mid = len(nums) // 2
        left_count, left_nums = self.subCountSmaller(start_idx, nums[:mid])
        right_count, right_nums = self.subCountSmaller(start_idx + mid, nums[mid:])
        new_nums = []
        left_idx, right_idx = 0, 0
        while len(new_nums) < len(nums):
            if left_idx >= len(left_nums):
                new_nums.extend(right_nums[right_idx:])
                break
            if right_idx >= len(right_nums):
                for i in range(left_idx, len(left_nums)):
                    new_nums.append(left_nums[i])
                    left_count[left_nums[i][1] - start_idx] += len(right_nums)
                break
            if left_nums[left_idx][0] <= right_nums[right_idx][0]:
                new_nums.append(left_nums[left_idx])
                left_count[left_nums[left_idx][1] - start_idx] += right_idx
                left_idx += 1
            else:
                new_nums.append(right_nums[right_idx])
                right_idx += 1
        return left_count + right_count, new_nums

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_idx = []
        for i, num in enumerate(nums):
            nums_idx.append([num, i])
        result, sorted_nums = self.subCountSmaller(0, nums_idx)
        return result

# https://blog.csdn.net/I_ren/article/details/105728206