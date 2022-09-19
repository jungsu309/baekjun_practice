T = int(input())

color_cost=[[0,0,0]]
dp=[[0,-1] for _ in range (1001)]#최대 1000번째 집까지 올수 있기때문. 1~1000을 표현하려면 1001번까지 자리를 내줘야한다.
#print(dp)
for t in range(T):
    color_cost.append(list(map(int, input().split())))

#print(color_cost)


#이번 행 작은거랑 다음행 작은거 더해서 작은거 고르기??

def DP(N):
    for i in range (1,(N+1),2):
        #print(i,"i (두개씩쌍으로 가자)")
        smallest = 1000

        #두행씩 생각해보자 -짝수번째에서 끝나게 해야함.
        for c in range(3):
            #print(dp[i-1],i-1)
            if c != dp[i-1][1]:
                now_cost = color_cost[i][c]
                #print(now_cost)
                now_index = c

                next_min_cost = min(color_cost[i+1])
                next_min_cost_index = color_cost[i+1].index(next_min_cost)

                if now_index != next_min_cost_index:
                    combine_cost = now_cost + next_min_cost
                    if combine_cost< smallest:
                        smallest = combine_cost
                        #작은걸 발견할때마다 넣어주기
                        dp[i][0] = dp[i-1][0]+now_cost
                        #print("내가 선택한거", now_cost, next_min_cost)
                        dp[i+1][0] = dp[i-1][0] + smallest
                        dp[i+1][1] = next_min_cost_index
                        #print(dp[:N+1])

                else:
                   #임시로 지금 최소값을 최대값으로대체해서 고르지 못하게 함.
                    #print("같을때?", now_index, now_cost, next_min_cost_index, next_min_cost)
                    color_cost[i+1][next_min_cost_index] = max(color_cost[i+1])
                    #최소값 다시 구하기
                    next_min_cost_modify = min(color_cost[i+1])
                    next_min_cost_index_modify = color_cost[i+1].index(next_min_cost_modify)

                    #다시 원상복귀 시켜주기(최소값이랑 최소값있는 인덱스 구했으니까 다시 원상복구해준다)
                    color_cost[i+1][next_min_cost_index] = next_min_cost

                    combine_cost = now_cost + next_min_cost_modify
                    if combine_cost< smallest:
                        smallest = combine_cost
                        #작은걸 발견할때마다 넣어주기
                        dp[i][0] = dp[i-1][0] + now_cost
                        dp[i+1][0] = dp[i-1][0] + smallest
                        #print("내가 선택한거(두번째로 작은거 골랐지만~)", now_cost, next_min_cost_modify)
                        dp[i+1][1] =  next_min_cost_index_modify
                        #print(dp[i+1][1])
                        #print(dp[:N+1])

if T %2 ==0:
    DP(T)
else:
    DP(T-1)
    #print(dp[:T+1])
    #마지막 인덱스와 겹치지 않는 작은 숫자 더해주기.
    last_c = dp[T-1][1]
    #print(last_c)

    last_min_cost = min(color_cost[T])
    #print(last_min_cost)
    last_min_cost_index = color_cost[T].index(last_min_cost)
    #print(last_min_cost_index)

    if last_c == last_min_cost_index:
        color_cost[T][last_min_cost_index] = max(color_cost[T])
        #최소값 다시 구하기
        last_min_cost_modify = min(color_cost[T])
        #last_min_cost_index_modify = color_cost[T].index(last_min_cost_modify)
        dp[T][0] = dp[T-1][0] + last_min_cost_modify
        #print(dp[T][0])
    else:
        dp[T][0] = dp[T-1][0] + last_min_cost
        
        
print(dp[T][0])
    
