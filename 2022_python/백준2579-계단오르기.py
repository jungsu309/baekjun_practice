#계단의 수
stair_n = int(input())
stair_li=[]
#자리 맞추려고
stair_li.append(0)
for s in range(stair_n):
    stair_li.append(int(input()))

#print(stair_li)

dp=[0]*(stair_n +1)


#지금 걸었을 떄
walk=[0]*(stair_n +1)
#지금 점프했을때
jump=[0]*(stair_n +1)

#초기세팅 
walk[1] = stair_li[1]
jump[1] = stair_li[1]
dp[1] = stair_li[1]
for i in range(2, stair_n+1):
    walk[i] = jump[i-1] + stair_li[i]
    jump[i] = dp[i-2] + stair_li[i]
    dp[i] = max(walk[i],jump[i])
#print(walk)
#print(jump)
#print(dp)
print(dp[stair_n])
    
    
