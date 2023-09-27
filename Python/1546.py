# 평균
# 자기 점수의 최댓값을 고른 후, 모든 점수에 점수/최댓값*100 을 한다.
# 첫째 줄에 시험 본 과목의 개수 N(<=1000)이 주어진다. 둘째 줄에 현재 성적(0~100, 적어도 하나의 값은 0보다 큼)이 주어진다.
# 새로운 평균을 출력한다.

n = input()
score = input()
origin_score = score.split()
edit_score = list()
total = 0

max = 0
for i in range(0, int(n)):
    if max <= int(origin_score[i]):
        max = int(origin_score[i])

for i in range(0, int(n)):
    if origin_score[i] != max:
        edit_score.append(int(origin_score[i]) / max * 100)
    else:
        edit_score.append(int(origin_score[i]))

for i in range(0, int(n)):
    total += edit_score[i]

avg = total / int(n)
print(avg)