class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [0] * n
        dp[-1] = max(1, 1 - dungeon[-1][-1])
        for j in range(n - 2, -1, -1):
            dp[j] = max(1, dp[j + 1] - dungeon[-1][j])
        for i in range(m - 2, -1, -1):
            dp[-1] = max(1, dp[-1] - dungeon[i][-1])
            for j in range(n - 2, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])
        return dp[0]

# https://maxming0.github.io/2020/06/21/Dungeon-Game/