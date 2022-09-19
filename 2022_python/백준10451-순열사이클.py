T = int(input())

def dfs(j,start):
    visit[j]=1
    check=0
    #print("방문처리하기",j)
    for k in range(N+1):
        #print("순회하기",k)
        if graph[j][k] !=0 and visit[k] ==0:
            if k ==start:
                #시작점으로 돌아왔을때
                break
            #print("발견!!",k)
            dfs(k,start)
    
            
for i in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    graph=[[0]* (N+1) for i in range(N+1)]
    visit=[0]*(N+1)
    
    i = 1
    for j in P:
        graph[i][j] = 1
        i = i+1
    #print(graph)
    cnt = 0
    
    for i in range(1,N+1):
        check=0
        for j in range(1,N+1):
            if check ==1:
                #print("뒤에 더 안봐두된다", j)
                break
            
            if graph[i][j] ==1 and visit[j] ==0:
                cnt = cnt+1
                check = 1
                visit[i]=1
                dfs(j,i)
                #print("한번 로테 돌았따",cnt)
                #print(visit)
    print(cnt)



    
