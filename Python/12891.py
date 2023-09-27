# DNA 비밀번호
# 첫 번째 줄에 민호가 임의로 만든 DNA 문자열 길이 |S|와 비밀번호로 사용할 부분문자열의 길이 |P| 가 주어진다. (1 ≤ |P| ≤ |S| ≤ 1,000,000)
# 두번 째 줄에는 민호가 임의로 만든 DNA 문자열이 주어진다.
# 세번 째 줄에는 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수가 공백을 구분으로 주어진다.
# 각각의 수는 |S| 보다 작거나 같은 음이 아닌 정수이며 총 합은 |S| 보다 작거나 같음이 보장된다.
# 첫 번째 줄에 민호가 만들 수 있는 비밀번호의 종류의 수를 출력해라.

checkList = [0] * 4     # 부분문자열에 포함되어야 할 최소 개수
myList = [0] * 4        # 부분문자열 문자의 개수
checkSecret = 0         # 부분문자열이 최소 개수를 넘었는지 확인하는 변수


# 문자 추가 함수
def myAdd(n):
    global checkList, myList, checkSecret
    if n == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif n == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif n == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif n == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1


# 문자 제거 함수
def myRemove(n):
    global checkList, myList, checkSecret
    if n == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif n == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif n == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif n == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


S, P = map(int, input().split())
A = list(input())
checkList = list(map(int, input().split()))
result = 0

for i in range(4):      # 최소 개수가 0으로 설정되어 있으면 함수에서 안돌기 때문에 미리 ++
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):      # 첫 번째 부분문자열 처리
    myAdd(A[i])

if checkSecret == 4:    # 부분문자열이 최소 개수를 넘었다면 결과++
    result += 1

for i in range(P, S):
    j = i - P
    myAdd(A[i])         # 새로운 문자 1개 추가
    myRemove(A[j])      # 맨 앞 문자 1개 제거
    if checkSecret == 4:    # 부분문자열이 최소 개수를 넘었다면 결과++
        result += 1

print(result)
