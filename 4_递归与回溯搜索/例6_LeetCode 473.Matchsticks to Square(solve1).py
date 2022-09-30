class Solution:
    def makesquare(self, nums):
        if len(nums) < 4:
            return False
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        if sum % 4:
            return False
        nums.sort(reverse=True)
        bucket = [0,0,0,0,0]
        return self.generate(0, nums, sum / 4, bucket)

    def generate(self, i, nums, target, bucket):
        if i >= len(nums):
            return bucket[0] == target and bucket[1] == target and bucket[2] == target and bucket[3] == target
        for j in range(4):
            if bucket[j] + nums[i] > target:
                continue
            bucket[j] += nums[i]
            if self.generate( i + 1, nums, target, bucket):
                return True
            bucket[j] -= nums[i]
        return False

# https://blog.csdn.net/fuxuemingzhu/article/details/79787660
