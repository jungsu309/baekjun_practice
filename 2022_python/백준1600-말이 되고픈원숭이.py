from collections import deque
from sys import stdin

dx=[2,2,1,1,-2,-2,-1,-1]
dy=[-1,1,-2,2,-1,1,-2,2]

dx2=[-1,1,0,0]
dy2=[0,0,-1,1]

#K번만 위와같이 이동가능
K = int(input())
W,H = map(int, input().split())

graph=[]
for h in range(H):
    graph.append(list(map(int, stdin.readline().split())))
visit = [[[0]*(K+1)  for _ in range(W)] for _ in range(H)]#세로, 가로, K 순

#맨처음
visit[0][0][K] = 1
move=deque()
#시작점=0,0(좌상단) 도착점=W-1, H-1(우하단)
#시작
move.append((0,0,0,K))#a,b,cnt,k순서. 말은 1에 갈 수 있기 때문에 2부터 시작해준다..
visit[0][0][K] = 1#시작상황(말로이동상태 K번남아있음)

def bfs(queue):
    while queue:
        x,y,c,k = queue.popleft()

        #목적지 도착시
        if x ==(H-1) and y ==(W-1):
            return c
        
        if k>0:#말로 이동가능한 상황
            for i in range(8):
                #말
                nx = x+dx[i]
                ny = y+dy[i]

                #범위내에 있고 같은 방법으로 방문했던곳인지 체크, 갈수있는 곳인지 확인
                if nx>-1 and nx<H and ny>-1 and ny<W and graph[nx][ny]==0 and visit[nx][ny][k-1]==0:
                    #print("말처럼 갈 수 있는곳",nx,ny)
                    queue.append((nx,ny,c+1, k-1))
                    visit[nx][ny] [k-1]= 1#방문 표시(말로갔으니까 한번 차감)
                    #print("말로 간곳",graph[nx][ny])
                    
        #k에 관계없이 항상 갈수 있음
        for j in range(4):
            nx2 = x+dx2[j]
            ny2 = y+dy2[j]
            if nx2>-1 and nx2<H and ny2>-1 and ny2<W and graph[nx2][ny2]==0 and visit[nx2][ny2][k] ==0:
                queue.append((nx2,ny2,c+1,k))
                visit[nx2][ny2][k] = 1#방문 표시
    #도착이 불가능하면
    return -1

print(bfs(move))
#도착지
#print(graph)

