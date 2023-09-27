# 구간 합 구하기 4
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오:
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
# 1 <= N <= 100,000
# 1 <= M <= 100,000
# a <= i <= j <= N

n, m = input().split()
n = int(n)
m = int(m)
num = input().split()
sum = [0]
result = list()

# 리스트 숫자로 변환
for i in range(0, n):
    num[i] = int(num[i])

sum.append(num[0])

# 합 배열 만들기
for i in range(1, n):
    sum.append(sum[ i ] + num[i])

# 결과 리스트에 저장
for i in range(0, m):
    a, b = input().split()
    a = int(a)
    b = int(b)
    result.append(sum[b] - sum[a-1])

# 출력
for i in range(0, m):
    print(result[i])