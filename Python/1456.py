# 거의 소수
# 어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.
# 두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력한다.
# 첫째 줄에 왼쪽 범위 A와 오른쪽 범위 B가 공백 한 칸을 사이에 두고 주어진다.
# 첫째 줄에 총 몇 개가 있는지 출력한다.

import math

m, n = map(int, input().split())
a = [0] * 10000001      # 시간복잡도를 위해 10^7까지만 수행 (문제 범위 10^14까지인데 제곱근만 찾으면 되기 때문)
for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a))) + 1):   # 시간복잡도를 위해 제곱근까지만 수행
    if a[i] == 0:
        continue
    for j in range(i + i, len(a), i):
        a[j] = 0

cnt = 0
for i in a:
    if i != 0:
        tmp = i * i
        while tmp <= n:
            if tmp >= m:
                cnt += 1
            tmp *= i

print(cnt)