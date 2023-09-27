# 최솟값 찾기
# N개의 수와 L이 주어진다. D(i) = A(i-L+1) ~ A(i) 중의 최솟값이라고 할 때, D에 저장된 수를 출력하시오.
# 첫째 줄에는 N, L이 주어지고, 둘째 줄에는 N개의 수가 주어진다.

from collections import deque

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
