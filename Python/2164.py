# 카드2
# N장의 카드가 순서대로 존재한다. 맨 윗장을 버리고, 다음 장을 맨 밑으로 넣는 작업을 반복한다.
# 마지막에 남는 카드의 숫자를 출력하시오.

from collections import deque

n = int(input())
myque = deque()

for i in range(1, n+1):
    myque.append(i)

while len(myque) != 1:
    myque.popleft()
    myque.append(myque.popleft())

print(myque[0])