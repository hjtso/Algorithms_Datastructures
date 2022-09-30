class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split()
        if len(pattern) != len(strs):
            return False
        d = dict()
        for i, p in enumerate(pattern):
            if p not in d:
                d[p] = strs[i]
            else:
                if d[p] != strs[i]:
                    return False
        d = dict()
        for i, p in enumerate(strs):
            if p not in d:
                d[p] = pattern[i]
            else:
                if d[p] != pattern[i]:
                    return False
        return True

# https://blog.csdn.net/fuxuemingzhu/article/details/72528424