# 신기한 소수
# 왼쪽부터 1자리, 2자리, ..., N자리 수 모두 소수인 수를 찾아라.
# 첫째 줄에 N이 주어진다. N자리 수 중에서 해당하는 소수를 찾아 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.

# 소수 판단 함수
def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True

# 깊이 우선 탐색 함수
def DFS(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10):
            # 현재 수에 i를 붙였을 때 홀수 && 소수인 경우만 출력
            if (num*10 + i) % 2 == 1 and isPrime(num*10 + i):
                DFS(num*10 + i)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

# 1의 자리 소수는 2 3 5 7만 존재하므로 이에 대해서만 실행
# DFS 함수를 실행하면, 해당 수에서 시작해서 뒷 자리에 숫자를 붙이며 탐색하므로 4가지 경우만 탐색하면 됨
DFS(2)
DFS(3)
DFS(5)
DFS(7)

