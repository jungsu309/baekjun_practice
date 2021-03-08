from collections import deque
N,M,K, X= map(int, input().split())

graph=[]
visited = [False]*N
#연결이 어떻게 되있는지 
for i in range(M):
    graph.append(list(map(int, input().split())))

queue = deque([X])
#첫 시작점
visited[X-1] = True

cnt = 0


while cnt<K:
    V = queue.popleft()
    cnt = cnt+1
    #V로 시작하는 도로가 있는지 없는지 보는 애
    is_start = False
    #X가 있는 리스트 찾기
    for i in range(M):
        if graph[i][0] == V:
            is_start = True
            if visited[graph[i][1]-1] == False:
                queue.append(graph[i][1])
                #방문으로 표시
                visited[graph[i][1]-1] = True
            else:
                queue.popleft()
                
if is_start ==False:
    print("-1")

else: 
    while queue:
        ans = queue.popleft()
        print(ans)


    
