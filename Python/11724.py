# 연결 요소의 개수
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if visited[i] == False:
            DFS(i)

for i in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1, n + 1):
    if visited[i] == False:
        cnt += 1
        DFS(i)

print(cnt)