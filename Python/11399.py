# ATM
# 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
# 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

n = int(input())
num = list(map(int, input().split()))

for i in range(1, n):
    min = 0
    tmp = num[i]
    for j in range(i - 1, -1, -1):
        if num[j] < num[i]:
            min = j + 1
            break
    for k in range(i, min, -1):
        num[k] = num[k - 1]
    num[min] = tmp

sum = [0] * (n + 1)
for i in range(n):
    sum[i + 1] = sum[i] + num[i]

result = 0
for i in range(n+1):
    result += sum[i]

print(result)