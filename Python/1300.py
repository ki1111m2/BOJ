# K번째 수
# 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.
# 첫째 줄에 배열의 크기 N이 주어진다. 둘째 줄에 k가 주어진다.
# B[k]를 출력하시오.

n = int(input())
k = int(input())
start = 1
end = k

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n + 1):
        # 한 열에서 중앙값보다 큰 수를 구하는 방법은 중앙값 / i
        # 한 열에 최대 n개기 때문에 중앙값 / i가 n보다 크다면 n을 저장
        cnt += min(mid // i, n)
    if cnt < k:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid

print(ans)