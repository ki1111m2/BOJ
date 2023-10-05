# 트리의 지름
# 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고(2 ≤ V ≤ 100,000), 둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 주어진다.
# 두 점 사이의 거리 중 가장 긴 것을 출력하시오.

# 너비 우선 탐색 함수
def BFS(v):
    visited[v] = True
    queue.append(v)
    while queue:
        a = queue.popleft()
        for i in A[a]:
            if visited[i[0]] == False:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[a] + i[1]

import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
A = [[] for _ in range(n + 1)]
# 거리 저장 리스트
distance = [0] * (n + 1)
# 방문 여부 리스트
visited = [False] * (n + 1)
queue = deque()

for i in range(n):
    data = list(map(int, input().split()))
    S = data[0]
    index = 1
    while True:
        E = data[index]
        if E == -1:
            break
        V = data[index + 1]
        A[S].append((E, V))
        index += 2

# 임의의 노드에서 실행 시작
BFS(1)

# 거리가 가장 긴 노드 찾기
max = 0
for i in range(1, n + 1):
    if distance[max] < distance[i]:
        max = i

# 초기화 후 가장 긴 노드에서 다시 탐색 시작
# 거리 저장 리스트
distance = [0] * (n + 1)
# 방문 여부 리스트
visited = [False] * (n + 1)
BFS(max)

# 거리 리스트 오름차순으로 정렬
distance.sort()
# 맨 끝 = 가장 먼 거리
print(distance[-1])