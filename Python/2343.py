# 기타 레슨
# 첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 블루레이의 개수 M (1 ≤ M ≤ N)이 주어진다. 다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다.
# 첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.

n, m = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0
for i in A:
    if start < i:
        start = i
    end += i

while start <= end:
    mid = (start + end) // 2
    sum = 0
    cnt = 0
    for i in range(n):
        if sum + A[i] > mid:
            # 블루레이 1개 증가
            cnt += 1
            sum = 0
        sum += A[i]
    if sum != 0:
        cnt += 1
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)