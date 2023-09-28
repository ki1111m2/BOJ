# 수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이며, 중복되지 않는다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
num = [0] * n
for i in range(n):
    num[i] = int(input())

for j in reversed(range(n)):
    for i in range(n - 1):
        if num[i] > num[i + 1]:
            tmp = num[i]
            num[i] = num[i + 1]
            num[i + 1] = tmp

for i in range(n):
    print(num[i])