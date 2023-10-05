# 수 찾기
# N개의 정수가 주어져 있으 ㄹ때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 첫째 줄에 자연수 N이 주어진다. 다음 줄에는 N개의 정수가 주어진다.
# 다음 줄에ㅔ는 M이 주어진다. 다음 줄에는 M개의 정수가 주어진다.
# M개의 수들이 N개의 수 안에 존재하는지 알아내시오.
# M개의 줄에 답을 출력하시오. 존재하면 1, 존재하지 않으면 0을 출력하시오.

n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
X = list(map(int, input().split()))

for i in X:
    find = False
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if i < A[mid]:
            end = mid - 1
        elif i > A[mid]:
            start = mid + 1
        else:
            find = True
            break
    if find == True:
        print(1)
    else:
        print(0)