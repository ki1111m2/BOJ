# 절댓값 힙
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            # 튜플의 형태로 저장되기 때문에 값을 꺼내기 위해선 [1]로 접근해야 함
            print(str((temp[1])) + '\n')
    else:
        # 절댓값으로 정렬 후 음수 > 양수 순서로 정렬
        myQueue.put((abs(request), request))