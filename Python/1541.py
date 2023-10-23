# 잃어버린 괄호
# 첫째 줄에 양수, +, -로 이루어진 식이 주어진다. 괄호를 적절히 이용하여 최소값을 만드시오.
# 첫째 줄에 정답을 출력하시오.

def Sum(i):
    B = list(i.split('+'))
    total = 0
    for k in B:
        total += int(k)
    return total

ans = 0
cnt = 0
A = list(input().split('-'))

for i in A:
    k = Sum(i)
    if cnt == 0:    # 첫 번째 값인 경우만 더하기
        ans += k
        cnt += 1
    else:
        ans -= k

print(ans)