n = int(input())

dp=[0]*1001
dp[1]=1

for i in range(2,n+1):
    #짝수일때
    if i%2 ==0:
        dp[i] = dp[i-1]*2 +1
    else:
        dp[i] = dp[i-1]*2 -1
print(dp[n]%10007)
