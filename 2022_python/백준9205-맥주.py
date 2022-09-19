from collections import deque

t = int(input())

def bfs(queue, n):
    while queue:
        x,y = queue.popleft()
        visit[0] = 1
        #지점 방문해보기
        for i in range(1, n+2):
            distance = abs(graph[i][0]-x) + abs(graph[i][1]-y)
            if distance <= 1000 and visit[i] ==0:
                visit[i]=1
                queue.append((graph[i][0], graph[i][1]))
    #락페 방문 표시가 없을때 - 못갔을때
    if visit[n+1] ==0:
        print("sad")
    else:
        print("happy")


                
for i in range(t):
    #편의점n
    n = int(input())
    #집
    graph=[]
    graph.append(list(map(int, input().split())))
    #편의점
    for i in range (n):
            graph.append(list(map(int, input().split())))
    graph.append(list(map(int, input().split())))

    visit=[0]*(n+2)#0 : 집 1~n:편의점 n+1:락페 

    #항상 맥주는 20병 유지 20병*50m = 1000 ->편의점 들린 직후 최대 1000만큼 갈 수있다
    #일단 집에서 1000 안쪽으로 갈수잇음
    #갈 수 있는곳부터 가보는 bfs를 써보자

    #graph = 집, 편의점 1~n, 락페
    #시작 = 집
    beer = deque()
    beer.append((graph[0][0], graph[0][1]))#순서대로 x,y

    bfs(beer, n)



        
    
