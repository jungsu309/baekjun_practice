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
visit = [[-1]*(W)  for _ in range(H)]#세로, 가로

#맨처음
move=deque()
#시작점=0,0(좌상단) 도착점=W-1, H-1(우하단)
#시작
move.append((0,0,0,K))#a,b,cnt,k순서. 말은 1에 갈 수 있기 때문에 2부터 시작해준다..

def bfs(queue):
    while queue:
        x,y,c,k = queue.popleft()
        #말처럼 이동
        if k>=1:#말로 이동가능한 상황
            for i in range(8):
                #말
                nx = x+dx[i]
                ny = y+dy[i]

                #범위내에 있고 같은 방법으로 방문했던곳인지 체크, 갈수있는 곳인지 확인
                if nx>-1 and nx<H and ny>-1 and ny<W and graph[nx][ny]==0:
                    if visit[nx][ny] ==-1 or visit[nx][ny]<k-1:#지금 이동하는게 말로 이동 덜한거일때?
                        if nx == H-1 and ny == W-1:#도착지점
                            return c + 1
                        visit[nx][ny] = k-1
                        queue.append((nx,ny,c+1, k-1))
                    
        #k에 관계없이 항상 갈수 있음
        for j in range(4):
            nx2 = x+dx2[j]
            ny2 = y+dy2[j]
            if nx2>-1 and nx2<H and ny2>-1 and ny2<W and graph[nx2][ny2]==0:
                if visit[nx2][ny2]==-1 or visit[nx2][ny2] < k:#지금이 더 말로 덜이동한 상태일때
                    if nx2 == H-1 and ny2 == W-1:#도착
                        return c +1
                    visit[nx2][ny2] = k
                    queue.append((nx2,ny2,c+1,k))
    #도착이 불가능하면
    return -1

if H ==1 and W ==1:
    print(0)
else:
    print(bfs(move))

