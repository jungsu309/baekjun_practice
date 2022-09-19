from collections import deque
#import sys
#sys.setrecursionlimit(3000000)

N,M = map(int,input().split())
graph=[]

for i in range(0,N):
    graph.append(list(map(int, input())))#붙어있는 경우 그냥 input을 사용하면 된다.
#print(graph)

#x,y를 좌표처럼 쓰기
#bfs는 재귀가 아니다. 큐를 이용하면서 큐가 빌때까지 돌리는 방법이다.
def bfs(a,b):
    queue = deque()
    #지금 있는 곳을 큐에 넣어준다.
    queue.append((a,b))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    #큐에 있는걸 꺼낸담에 조건에 만족하게 되면 큐에 넣어준다.
    while queue:
        #일단 지금 큐에 잇는걸 꺼냄
        x,y = queue.popleft()#xy 두개라서 따로따로 저장이 가능
        #4방향-> 리스트이용..!!
        for i in range(0,4):
            move_x = x + dx[i]
            move_y = y + dy[i]
            #이동했을때 1이면서 범위 안에 있어야함.
            if move_x >=0 and move_x <N and move_y >= 0 and move_y <M and graph[move_x][move_y] ==1:
                #해당하니까 queue에 다시 넣어준다 (나중에 다시 꺼내서 방문하려고)
                queue.append((move_x, move_y))
                #들렸던 길 표시
                graph[move_x][move_y]=graph[x][y]+1
bfs(0,0)
print(graph[N-1][M-1])#최종지점
#print(graph[0][0])
