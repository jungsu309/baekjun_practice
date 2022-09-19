from collections import deque
import copy

N = int(input())

colors_3=[]
#적록색 R=G
colors_2=[]

for i in range(N):
    color=list(map(str, input()))
    colors_3.append(color)
    
#서로 다른 개별로 쓰려면 깊은복사가필요하다!
colors_2 = copy.deepcopy(colors_3)
#print(colors_3)
#print(colors_2)

dx=[-1,1,0,0]
dy = [0,0,-1,1]

Q_3=deque()
Q_2=deque()

cnt_3 = 0
cnt_2 = 0


def bfs(queue,graph,color):
    while queue:
        x,y = queue.popleft()
        #방문처리
        graph[x][y]='X'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if len(color) == 2:#R,G 같은걸로 볼때
                if nx >-1 and nx <N and ny >-1 and ny <N and (graph[nx][ny] == color[0] or graph[nx][ny] == color[1]):
                    queue.append((nx,ny))
                    graph[nx][ny] = 'X'#방문표시
                    
            if nx >-1 and nx <N and ny >-1 and ny <N and graph[nx][ny] == color:
                queue.append((nx,ny))
                graph[nx][ny] = 'X'#방문표시

                
for i in range(N):
    for j in range(N):
        if colors_3[i][j] == 'R':
            Q_3.append((i,j))
            bfs(Q_3,colors_3,'R')
            cnt_3 = cnt_3+1
        elif colors_3[i][j] == 'G':
            Q_3.append((i,j))
            bfs(Q_3,colors_3,'G')
            cnt_3 = cnt_3+1
        elif colors_3[i][j] == 'B':
            Q_3.append((i,j))
            bfs(Q_3,colors_3,'B')
            cnt_3 = cnt_3+1
        #적록색약의 경우
        if colors_2[i][j] == 'R' or colors_2[i][j] == 'G':
            Q_2.append((i,j))
            bfs(Q_2, colors_2, ['R','G'])
            cnt_2 = cnt_2+1
        elif colors_2[i][j] == 'B':
            
            Q_2.append((i,j))
            bfs(Q_2,colors_2,'B')
            cnt_2 = cnt_2+1


print(cnt_3, cnt_2)        

#print(colors_3)
#print(colors_2)            

        
    
