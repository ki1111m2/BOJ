# 회의실 배정
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
# 첫째 줄에 회의의 수 N, 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어진다. 이는 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

n = int(input())
A = [[0, 0] for _ in range(n)]

for i in range(n):
    S, E = map(int, input().split())
    A[i][0] = E     # 종료시간을 기점으로 정렬해야 하기 때문에 앞에 저장
    A[i][1] = S

A.sort()
cnt = 0
end = -1

for i in range(n):
    if A[i][1] >= end:
        cnt += 1
        end = A[i][0]

print(cnt)