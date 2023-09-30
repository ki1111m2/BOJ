# 수 정렬하기 2
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


# 병합 정렬 함수
def merge(s, e):
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
        if tmp[index1] < tmp[index2]:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
        else:
            A[k] = tmp[index2]
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
print = sys.stdout.write

n = int(input())
A = []
tmp = [0] * n

for i in range(n):
    A.append(int(input()))

merge(0, n - 1)

for i in range(n):
    print(str(A[i]) + '\n')