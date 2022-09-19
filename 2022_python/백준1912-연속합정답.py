n= int(input())

li = list(map(int, input().split()))
#print(li)

dp=[0]*(n)
dp[0] = li[0]#첫번째 자리 초기화
#누적합 구하기
for i in range (1,n):
    #print(li[i], dp[i-1] + li[i])
    dp[i] = max(li[i], dp[i-1] + li[i])
    #print(dp[i])
print(dp)
print(max(dp))

