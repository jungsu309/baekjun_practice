#레벨의 수N
N = int(input())

score=[]
for i in range(0,N):
    score.append(int(input()))
#print(score)

#뒤에서부터 해보자
now=score[N-1]
answer = 0
for i in range(N-1, 0,-1):
    if now <= score[i-1]:
        answer = answer + (score[i-1] -now) +1
        #print(answer)
        now = now - 1
    else :# 4 5나 3 5처럼 앞이 작을때 다음 계산을 위해 now 업데이트    
        now = score[i-1]

print(answer)
