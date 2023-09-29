# K번째 수
# 수 N개가 주어진다. 오름차순 정렬했을 때, 앞에서부터 K번째에 있는 수를 구하시오.
# 첫째 줄에 수의 개수 N과 수의 위치 K가 주어진다. 둘째 줄에 N개의 수가 주어진다. K번째 수를 출력하시오.

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 위치 변경 함수
def swap(i, j):
    global A
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

# pivot 값과 위치 구하는 함수
def partition(S, E):
    global A
    # 요소가 2개라면 바로 정렬
    if E - S == 1:
        if A[S] > A[E]:
            swap(S, E)
        return E

    # 중앙값을 pivot으로 설정
    M = (S + E) // 2
    # 편리한 계산을 위해 pivot을 첫번째 위치와 변경
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E

    while i <= j:
        # 2-1) start가 가리키는 데이터가 pivot이 가리키는 데이터보다 작으면 start를 오른쪽으로 1칸 이동
        while A[i] < pivot and i < len(A) - 1:
            i += 1
        # 2-2) end가 가리키는 데이터가 pivot이 가리키는 데이터보다 크면 end를 왼쪽으로 1칸 이동
        while A[j] > pivot and j > 0:
            j -= 1
        # 2-3) start, end가 가리키는 데이터를 swap하고 start는 오른쪽, end는 왼쪽으로 1칸씩 이동
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1

    A[S] = A[j]
    A[j] = pivot
    return j

# 퀵 정렬 함수
def quick(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:
            return
        elif pivot > K:
            quick(S, pivot - 1, K)
        else:
            quick(pivot + 1, E, K)

quick(0, N - 1, K - 1)
print(A[K - 1])