# 수 묶기
# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다.
# 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다. 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.
# 첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수이다. 둘째 줄부터 N개의 줄에 수열의 각 수가 주어진다. 수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
# 수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 정답은 항상 231보다 작다.

from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()
nq = PriorityQueue()
zero = 0
one = 0
for i in range(n):
    data = int(input())
    if data > 1:
        # 내림차순 정렬을 위해 -1을 곱해서 저장
        pq.put(data * -1)
    elif data < 0:
        nq.put(data)
    elif data == 0:
        # 0의 경우 곱하지 않고 더하는게 더 큰 수를 만듦
        # 음수는 0을 곱하는게 더 큰 수를 만듦
        zero += 1
    elif data == 1:
        # 1의 경우 곱하지 않고 더하는게 더 큰 수를 만듦
        one += 1

sum = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    sum += data1 * data2

while nq.qsize() > 1:
    data1 = nq.get()
    data2 = nq.get()
    sum += data1 * data2

if pq.qsize() != 0:
    data = pq.get() * -1
    sum += data

if nq.qsize() != 0 and zero == 0:
    # 음수와 곱할 0이 남아있지 않다면 합에 추가
    data = nq.get()
    sum += data

sum += one
print(sum)