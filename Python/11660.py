# 구간 합 구하기 5
# N*N개의 수가 N*N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.
# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2가 주어진다.
# 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
origin = list()
result = list()

# 원본 배열 입력
for i in range(0, n):
    a = list(map(int, input().split()))
    origin.append(a)

# 합배열 생성
sum = [[0]*(n+1) for i in range(n+1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1] + origin[i - 1][j - 1]

# x1, y1, x2, y2 입력
for i in range(0, m):
    x1, y1, x2, y2 = map(int, input().split())
    result.append(sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1])

# 결과 출력
for i in range(0, m):
    print(result[i])