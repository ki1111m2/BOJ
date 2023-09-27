# 좋다
# N개의 수 중 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있으면 그 수를 '좋다'고 한다.
# N개의 수 중 몇 개가 좋은 수인지 출력하시오. 수가 같아도 위치가 다르면 다른 수이다.
# 첫째 줄에는 수의 개수 N, 둘째 줄에는 N개의 수가 주어진다.


import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0

for k in range(n):
    i = 0
    j = n - 1
    while i < j:
        if num[i] + num[j] == num[k]:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            else:
                j -= 1
        elif num[i] + num[j] > num[k]:
            j -= 1
        else:
            i += 1

print(cnt)