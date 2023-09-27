# 주몽
# 두 숫자를 합쳐 M이 되어야 한다. N개의 숫자와 M이 주어졌을 때 몇 개의 조합이 만들어지는지 구하시오.
# 첫째 줄에는 숫자의 개수N이 주어진다. 두 번재 줄에는 M이 주어진다. 세 번째 줄에는 N개의 숫자들이 공백을 가지고 주어진다.
# 개수를 출력하시오.

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0
i = 0
j = n - 1

while i < j:
    if num[i] + num[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif num[i] + num[j] > m:
        j -= 1
    else:
        i += 1

print(cnt)