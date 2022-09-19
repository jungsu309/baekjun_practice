from sys import stdin
from collections import deque
M ,N = map(int, input().split())
#print(M,N)
box = []
for i in range(0,N):
    box.append(list(map(int, stdin.readline().split())))
#print(box)

#퍼져나가는 형식이고, 최소날짜를 구해야 하니까 bfs가 맞는것 같다
dx = [-1,1,0,0]
dy=[0,0,-1,1]
#시작점 구하기 -> 좌표가 1인 곳
startpoint = deque()
for i in range(0,N):
    for j in range(0,M):
        if box[i][j] ==1:
            startpoint.append((i,j))
#날짜
cnt =0
def bfs(graph, queue, N, M):
    global cnt
    while queue:
        #print(queue)
        for i in range(len(queue)):
            x,y = queue.popleft()
            #추출한거 주변 훑기
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                #0~N, 0~M 사이에 있으면서 0이면 1로 바꿔주기
                if nx > -1 and nx < N and ny > -1 and ny < M and graph[nx][ny]==0:
                    #익는다!
                    graph[nx][ny]=1
                    queue.append((nx,ny))
        cnt = cnt+1

    #전부 다 한 다음에 while문 나와서, 만약 0이 남아있다면 전부 다 익힐 수 없는거다.
    for i in range(0,N):
        for j in range(0,M):
            #익히지못한 토마토 발견
            if graph[i][j] == 0:
                cnt =0
                break

bfs(box, startpoint, N, M)
print(cnt-1)#첫날 제외 
