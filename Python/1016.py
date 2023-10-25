# 제곱 ㄴㄴ 수
# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다.
# 첫째 줄에 두 정수 min과 max가 주어진다.
# 첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

import math

min, max = map(int, input().split())
check = [False] * (max - min + 1)

for i in range(2, int(math.sqrt(max)) + 1):
    now = i * i
    start = min // now
    if min % now != 0:
        start += 1
    for j in range(start, max // now + 1):
        check[int(j * now - min)] = True

cnt = 0

for i in range(0, max - min + 1):
    if check[i] == False:
        cnt += 1

print(cnt)