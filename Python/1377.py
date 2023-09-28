# 버블 소트
# swap이 한 번도 일어나지 않은 구간을 찾으시오.
# 첫째 줄에 N이 주어진다. 둘째 줄부터 N개의 줄에 값이 하나씩 주어진다. N은 500,000보다 작거나 같은 자연수이다.
# 정답을 출력하시오.

import sys
input = sys.stdin.readline

n = int(input())
origin = []
for i in range(n):
    origin.append((int(input()), i))
sorted = sorted(origin)
num = [0] * n

for i in range(n):
    num[i] = sorted[i][1] - i + 1

print(max(num))