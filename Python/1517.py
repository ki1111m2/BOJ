# 버블 소트
# N개의 수로 이루어진 수열에 대해서 버블 소트를 수행할 때, 총 몇 번의 swap이 발생하는지 알아내시오.
# 첫째 줄에 N이 주어진다. 둘째 줄에 N개의 수가 주어진다. 총 swap 횟수를 출력하시오.

# 병합 정렬 함수
def merge(s, e):
    global cnt
    # 그룹의 개수가 2개 미만이면 종료
    if e - s < 1: return

    # 그룹 나눌 위치 설정
    m = int(s + (e - s) / 2)
    # 나눈 위치 기준으로 앞 뒤 그룹 각각 병합 정렬
    merge(s, m)
    merge(m + 1, e)

    # 임시 배열에 현재 배열 상태 저장
    for i in range(s, e + 1):
        tmp[i] = A[i]

    # 배열이 입력될 인덱스
    k = s
    index1 = s
    index2 = m + 1

    while index1 <= m and index2 <= e:
        # 둘 중에 작은 인덱스를 배열에 저장
        if tmp[index1] <= tmp[index2]:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
        else:
            A[k] = tmp[index2]
            # 뒷 그룹의 요소가 선택되는 경우에만 역전이 일어나므로 cnt++
            cnt = cnt + index2 - k
            k += 1
            index2 += 1
    # 두 그룹 중 한 그룹이 끝났다면 나머지 그룹은 그대로 저장
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
tmp = [0] * n
cnt = 0

merge(0, n - 1)

print(cnt)