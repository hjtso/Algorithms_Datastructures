class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N=len(M)
        seen=set()
        def dfs(node):
            for i, j in enumerate(M[node]):
                if j and i not in seen:
                    seen.add(i)
                    dfs(i)
        ans=0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans+=1
        return ans

# https://blog.csdn.net/Orientliu96/article/details/104200380
