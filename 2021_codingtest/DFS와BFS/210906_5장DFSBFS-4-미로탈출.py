#20210906 5장 DFS/BFS 4 미로 탈출

#괴물을 피해서 가기. 최소경로 구하기. 출구는 대각선 경로에있는 (N,M)위치. 
#괴물이 잇는게 0 없는게 1

#N:세로길이  M:가로길이

from collections import deque
N,M = map(int, input().split())

array_2=[]

for n in range(N):
   array_2.append(list(map(int, input())))

#x가 세로, y가 가로. 순서대로 상하좌우임
dx = [1,-1,0,0]
dy = [0,0,-1,1]

#최단경로 찾는것은 BFS가 빠르다고 한다. 근처에있는거를 하나씩 찾기 때문..이라고 함.
def bfs(graph, x, y):
    #bfs니까 큐 만들기
    queue=deque()
    #첫 시작점 넣기. 쌍으로 넣으려면 ()에 넣어주기
    queue.append((x,y))
    #큐가 빌때까지 계속 수행. 큐가 비면 전체 수행이 끝난것이다.
    while queue:
        #지금 위치 꺼 빼서 그거로 상하좌우 살피기
        x,y = queue.popleft()
        #구현에서 했던거처럼 상하좌우 살펴보고 괴물이 없으면 전진하0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #비교하기 전에 범위를 벗어나는 경우 무시함
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            #가도되는 길이면 큐에 추가해주기
            if graph[nx][ny] == 1:
                #해당 노드 방문할때마다 +1 해줘서 방문 횟수 기록해준다.
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지 최단거리 반환 이라는데 이렇게 한다고 잘 가나???
    #가장오른쪽 끝까지 오면 더이상 진행안하고 끝내는건 이해하겠는데 방향이 잘못된곳으로 잡히면 어떻게 되는거임? 잘 모르겠다.
    return  graph[N-1][M-1]

print(bfs(array_2, 0, 0))
            
        
