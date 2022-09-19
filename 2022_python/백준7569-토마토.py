from sys import stdin
from collections import deque
#가로/세로/높이
M,N,H = map(int, input().split())

box=[]
for i in range(H):
    #한층
    h=[]
    for j in range(N):
        h.append(list(map(int, stdin.readline().split())))
    box.append(h)
#print(box)

dx = [-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
cnt = 0

def bfs(queue, graph):
    global cnt
    while queue:
        #print("큐 갯수",len(queue))
        for i in range (len(queue)):#이게 있어야지 하루치만 셀수 있음
            z,y,x = queue.popleft()
            for i in range(6):
                nx = x+dx[i]
                ny = y+dy[i]
                nz = z+dz[i]
                if nx>-1 and nx<M and ny >-1 and ny<N and nz>-1 and nz<H and graph[nz][ny][nx] ==0:
                    graph[nz][ny][nx]=1
                    queue.append((nz,ny,nx))

        cnt = cnt+1


tomato=deque()
#x = 가로 =M // y = 세로=N// z=높이 = H

for h in range(H):
    for n in range(N):
        for m in range(M):
            #순서대로 높이 가로 세로
            if box[h][n][m] == 1:
                #시작할때 토마토 있는 곳
                tomato.append((h,n,m))
            
bfs(tomato, box)

#print(box)
#다 하고나서 0이 있는경우...-또 포문 돌아야하냐
for h in range(H):
    for n in range(N):
        for m in range(M):
            #순서대로 높이 가로 세로
            if box[h][n][m] == 0:
                cnt = 0
                break

print(cnt-1)
