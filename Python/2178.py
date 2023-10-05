# 미로 탐색
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다.

# 너비 우선 탐색 함수
def BFS(i, j):
    visited[i][j] = True
    queue.append((i, j))
    # 큐가 비기 전까지 반복
    while queue:
        a = queue.popleft()
        for k in range(4):
            x = a[0] + dx[k]
            y = a[1] + dy[k]
            if x >= 1 and y >= 1 and x <= n and y <= m:
                if A[x][y] == 1 and visited[x][y] == False:
                    visited[x][y] = True
                    # 현재 위치까지 오는데 몇 번이나 걸렸는지
                    A[x][y] = A[a[0]][a[1]] + 1
                    queue.append((x, y))

import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
# 데이터 저장
A = [[0] for _ in range(n + 1)]
for i in range(1, n + 1):
    a = input()
    for j in range(m):
        A[i].append(int(a[j]))

visited = [[False] * (m + 1) for _ in range(n + 1)]
queue = deque()

# 상하좌우 탐색을 위한 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

BFS(1, 1)
print(A[n][m])