# 소트인사이드
# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

n = input()
num = []

for i in range(len(n)):
    num.append(int(n[i]))

for i in range(len(n)):
    max = i
    for j in range(i + 1, len(n)):
        if num[j] > num[max]:
            max = j
    if num[i] < num[max]:
        tmp = num[i]
        num[i] = num[max]
        num[max] = tmp

for i in range(len(n)):
    print(num[i], end='')