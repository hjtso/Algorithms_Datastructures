import heapq
import sys

MAX_N = 10000

# 入力
L, P, N = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 簡単なためゴールをガソリンスタンドに追加
A += [L]
B += [0]
N += 1

# ガソリンスタンドを管理する順位キュー
que = []

# ans：補給回数, pos：今いる場所, tank：タンクのガソリンの量
ans = 0
pos = 0
tank = P

for i in range(N):
    # 次に進む距離
    d = A[i] - pos

    # 十分な量になるまでガソリンを補給
    while tank - d < 0:
        if len(que) == 0:
            print("-1")
            sys.exit()
        tank += -1 * heapq.heappop(que)
        ans += 1

    tank -= d
    pos = A[i]
    heapq.heappush(que, -1 * B[i])

print(ans)

# https://kuruton.hatenablog.com/entry/2020/11/02/080000