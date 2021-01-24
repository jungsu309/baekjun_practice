T = int(input())


score=[]

score = list(map(int,input().split()))

#최댓값 구하기

MAX = 0

for n in range(0, len(score)):
    if MAX > score[n]:
        MAX = MAX
    elif MAX < score[n]:
        MAX = score[n]

#값 변경하기
change_score=[]
for k in score:
    change_score.append(k*100/MAX)

#평균구하기
sum = 0
for m in change_score:
    sum = sum + m

avg = sum/T

print(avg)
