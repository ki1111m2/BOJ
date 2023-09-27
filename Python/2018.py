# 수들의 합 5
# 어떠한 자연수 N은 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 이 N에 대해서 몇 개의 연속된 자연수의 합으로 나타낼 수 있는지 가지수를 알고 싶다.
# 첫 줄에 정수 N이 주어진다. 가지수를 출력하시오.

n = int(input())
start = 1
end = 1
sum = 1
cnt = 1

while end != n:
    if sum == n:
        cnt += 1
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(cnt)