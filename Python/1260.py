# DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
# 첫째 줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 첫째 줄에 DFS를 수행한 결과를, 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 깊이 우선 탐색 함수
def DFS(v):
    visited[v] = True
    print(v, end=' ')
    answer_DFS.append(v)
    for i in A[v]:
        if visited[i] == False:
            DFS(i)

# 너비 우선 탐색 함수
def BFS(v):
    visited[v] = True
    print(v, end=' ')
    queue.append(v)
    # 큐가 비기 전까지 반복
    while queue:
        a = queue.popleft()
        answer_BFS.append(a)
        for i in A[a]:
            if visited[i] == False:
                visited[i] = True
                print(i, end=' ')
                queue.append(i)

import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, v = map(int, input().split())
# 인접 리스트
A = [[] for _ in range(n + 1)]

for i in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

# 작은 수부터 출력하기 위해 정렬
for i in range(n + 1):
    A[i].sort()

# 방문 여부 확인
visited = [False] * (n + 1)
answer_DFS = []
DFS(v)

print()

# 방문 여부 확인
visited = [False] * (n + 1)
answer_BFS = []
queue = deque()
BFS(v)