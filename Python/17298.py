# 오큰수
# A[i]에 대해 오른쪽에 있는 수 중 A[i]보다 크면서 가장 왼쪽에 있는 수를 오큰수라고 한다.
# N개의 수가 주어졌을 때 이들의 오큰수를 모두 출력하시오.

n = int(input())
array = list(map(int, input().split()))
stack = []
result = [0] * n

for i in range(n):
    # 스택이 비어있지 않고, top 번호의 배열 값이 현재 배열 값보다 작다면, top 번호의 오큰수는 현재 배열 값
    while stack and array[stack[-1]] < array[i]:
        result[stack.pop()] = array[i]
    # 스택이 비어있거나, top 번호의 배열 값이 현재 배열 값보다 크다면, 스택에 현재 값 인덱스 추가
    stack.append(i)

while stack:
    # 작은 수들은 모두 스택에서 빠졌기 때문에, 스택에 남아있는 수들은 오큰수가 없는 수
    result[stack.pop()] = -1

for i in range(n):
    print(result[i], end=' ')