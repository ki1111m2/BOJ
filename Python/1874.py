# 스택 수열
# 1 ~ n까지의 수를 이용해 수열을 만든다. 스택의 연산을 이용하여 만들 수 있는지 판단하라.
# 스택에는 오름차순으로 입력되며, 수열은 1 이상 n 이하의 정수로 이루어져 있으며, 같은 수가 두 번 나오는 일은 없다.
# push 연산은 +로, pop 연산은 -로, 불가능하다면 NO를 출력한다.

n = int(input())
array = [0] * n

for i in range(n):
    array[i] = int(input())

stack = []
num = 1
answer = []
result = True

for i in range(n):
    # 필요한 수가 현재 자연수보다 크다면 스택에 자연수 삽입 및 자연수++
    while array[i] >= num:
        stack.append(num)
        num += 1
        answer.append('+')

    # 스택의 끝 요소가 필요한 수의 값과 같다면 삭제
    if stack[-1] == array[i]:
        stack.pop()
        answer.append('-')

    # 스택의 끝 요소가 필요한 요소와 다르다면 불가능
    else:
        print('NO')
        result = False
        break


if result:
    for i in answer:
        print(i)