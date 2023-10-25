# 소수 & 팰린드롬
# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다.  N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N이 주어진다.
# 첫째 줄에 조건을 만족하는 수를 출력한다.

def Pal(x):
    num = str(x)
    mid = len(num) // 2
    for i in range(mid):
        if num[i] != num[-i - 1]:
            return False
    return True

import math
n = int(input())
a = [0] * 10000001
for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a))) + 1):   # 시간복잡도를 위해 제곱근까지만 수행
    if a[i] == 0:
        continue
    for j in range(i + i, len(a), i):
        a[j] = 0

while True:
    if a[n] != 0:
        if Pal(n) == True:
            print(n)
            break
    n += 1