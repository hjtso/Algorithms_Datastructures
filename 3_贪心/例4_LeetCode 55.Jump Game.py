class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = []
        for i in range(len(nums)):
            index.append(i + nums[i])
        jump = 0
        max_index = index[0]
        while jump < len(index) and jump <= max_index:
            if max_index < index[jump]:
                max_index = index[jump]
            jump += 1
        if jump == len(index):
            return True
        return False
