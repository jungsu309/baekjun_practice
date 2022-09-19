from collections import deque

#사람수
n = int(input())

#알고싶은 촌수
x, y = map(int, input().split())
#관계수
m = int(input())

#0포함되는거 버리려고 1칸씩 늘려
graph = [[0]*(n+1) for _ in range(n+1)]
relationship=[]
visit=[-1]*(n+1)#초기에 아무와도 관계 없는것으로 표현
Q = deque()

for i in range(m):
    relationship.append(list(map(int, input().split())))
    #연결리스트를 그래프로 표현하기. 쌍방향임
    #print(relationship[i][0])
    graph[relationship[i][0]][relationship[i][1]]=1
    graph[relationship[i][1]][relationship[i][0]]=1
#print(relationship)
#print(graph)
    


def bfs(a,b, queue,visit):
    while queue:
        x = queue.popleft()
        #print("x" ,x)
        for i in range(1,n+1):
            if graph[x][i] == 1 and visit[i]==-1:
                #촌수 증가
                visit[i] = visit[x]+1
                queue.append((i))

    
    #print(visit)
    #우리가 알고싶은 값
    print(visit[b])

    
#관계를 알고싶은 x y를 넣어주기
Q.append((x))
visit[x]=0
bfs(x,y,Q,visit)



    
