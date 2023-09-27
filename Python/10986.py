# 나머지 합
# N개의 수가 주어진다. 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
# 즉 A(j) + ... + A(i) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.
# 첫째 줄에 N, M이 주어진다. 둘째 줄에 N개의 수가 주어진다.
# 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

# 수 입력
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
origin = list(map(int, input().split()))
cnt = 0

# 구간합 생성
sum = [0]
for i in range(n):
    sum.append(sum[i] + origin[i])

# 구간합 수정 (M으로 나눈 나머지)
for i in range(n + 1):
    sum[i] %= m

# 나머지 별로 개수 세어진 배열 생성
remain = [0 for i in range(m)]
for i in range(1, n + 1):
    z = sum[i] % m
    if z == 0:  # 나머지가 0이라면 정답 += 1
        cnt += 1
    remain[z] += 1

# 나머지가 같은 경우 중 2개를 뽑는 경우의 수 계산
for i in range(m):
    if remain[i] > 1:
        cnt += remain[i] * (remain[i] - 1) // 2

print(cnt)
