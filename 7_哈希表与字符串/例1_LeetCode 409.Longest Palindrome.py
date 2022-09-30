import collections

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        res = 0
        flag = 0
        for k, v in count.items():
            if v % 2 == 1:
                res += v - 1
                flag = 1
            else:
                res += v
        return res + flag

# https://blog.csdn.net/fuxuemingzhu/article/details/54236594