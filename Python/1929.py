# 소수 구하기
# M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import math

m, n = map(int, input().split())
a = [0] * (n + 1)
for i in range(2, n + 1):
    a[i] = i

for i in range(2, int(math.sqrt(n)) + 1):   # 시간복잡도를 위해 제곱근까지만 수행
    if a[i] == 0:
        continue
    for j in range(i + i, n + 1, i):
        a[j] = 0

for i in a:
    if i >= m and i <= n and i != 0:
        print(i)