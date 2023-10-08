# 카드 정렬하기
# 정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다.
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.
# 첫째 줄에 최소 비교 횟수를 출력한다.

from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()

for i in range(n):
    queue.put(int(input()))

sum = 0

while queue.qsize() > 1:
    data1 = queue.get()
    data2 = queue.get()
    now = data1 + data2
    sum += now
    queue.put(now)

print(sum)