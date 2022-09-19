T = int(input())


dp=[0]*12#1~11 까지 담아야하니까
dp[1]=1
dp[2]=2
dp[3]=4
problem=[]
for i in range(T):
    problem.append(int(input()))

#print(problem)

#전부 넣어주고 그냥 원하는 부분을 뽑을까?
def DP(n):
    
    for i in range(1,n):
        #먼가 계산된 값이 들어가 있을때-> pass
        if dp[i] ==0:
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]

DP(len(dp))
#print(dp)

for p in problem:
    print(dp[p])
