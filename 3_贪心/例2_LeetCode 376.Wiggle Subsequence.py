class Solution(object):
    def wiggleMaxLength(self, nums):
        BEGIN = 0
        UP = 1
        DOWN = 2

        state = BEGIN
        max_length = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if i == 0:
                continue
            if state == BEGIN:
                if nums[i - 1] < nums[i]:
                    state = UP
                    max_length += 1
                elif nums[i - 1] > nums[i]:
                    state = DOWN
                    max_length += 1
            elif state == UP:
                if nums[i - 1] > nums[i]:
                    state = DOWN
                    max_length += 1
            elif state == DOWN:
                if nums[i - 1] < nums[i]:
                    state = UP
                    max_length += 1

        return max_length

# http://bookshadow.com/weblog/2016/07/21/leetcode-wiggle-subsequence/