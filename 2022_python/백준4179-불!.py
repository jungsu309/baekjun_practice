from collections import deque

R,C = map(int, input().split())
#print(R,C)

maze=[]
for r in range (0, R):
    maze.append(list(map(str, input())))
#print(maze)

jihun = deque()
fire=deque()
#지훈 시작점, 불 시작점 저장
for i in range(0,R):
    for j in range(0,C):
        if maze[i][j] == 'J':
            jihun.append((i,j))
        if maze[i][j] == 'F':
            fire.append((i,j))
            
dx = [-1,1,0,0]
dy= [0,0,-1,1]
#지훈이가 더이상 움직이지 못할때, 탈출이 가능한경우 t여기다 담아주자.
escape=[]


#최단 거리 니까 아마도 BFS 쓰면 될 것같다.
#불도 사방으로, 지훈이도 사방으로 이동한다.
#불은 확정적으로 사방(네방향 모두)으로 이동하므로 확정적이다. 그리고 불은 여러공간에 있을수있음
#지훈이는 불을 피해서 사방중 한곳으로 이동이 가능하다. J는 하나이다.
move = 0#이동횟수
def bfs(maze, escape):
    global move
    #지훈이가 갈 곳이 있을때까지 반복해보자-갈곳이 없으면 종료
    while jihun:
        #불 먼저 확산시키기
        #print("불 확산",fire)
        for i in range (len(fire)):
            f_x, f_y = fire.popleft()
            for f in range(0, 4):
                f_nx = f_x + dx[f]
                f_ny = f_y + dy[f]
                #불 붙을 수 잇는 곳 찾기- 이동하기전인 J자리까지 침범이 가능
                if f_nx > -1 and f_nx < R and f_ny > -1 and f_ny < C and maze[f_nx][f_ny] != '#' and maze[f_nx][f_ny] != 'F':
                    maze[f_nx][f_ny] = 'F'#불 확산
                    fire.append((f_nx, f_ny))
                    
        #불이 다 옮겨 붙었을때, 지훈이가 이동할수 있는 곳 찾기
        #-지훈이도 여러곳 있을 수 있다. 가능한 경로를 찾는 중에는 가능함.
        #print("지훈이 현재(예상)위치 ", jihun)
        #print(move)
        for k in range(len(jihun)):
            j_x, j_y = jihun.popleft()
            #지훈이의 위치가 탈출이 가능한 위친지 확인하기
            if j_x == 0 or j_x == (R-1) or j_y == 0 or j_y == (C-1):
                #print("탈출이 되는 상황", j_x, j_y)
                escape.append(move+1)#다음 번에 탈출이 가능한 경우
            for j in range(0,4):
                j_nx = j_x + dx[j]
                j_ny = j_y + dy[j]
                #지훈이가 이동할 수 있는 곳 찾기->.인곳으로 이동하거나
                if j_nx > -1 and j_nx < R and j_ny > -1 and j_ny < C and maze[j_nx][j_ny] == '.' and maze[j_nx][j_ny] != 'J':
                        #print("점이 잇는곳으로 이동")
                        maze[j_nx][j_ny] = 'J'#지훈이가 잇을 수 있는곳. 경우의 수에서 겹쳐도 상관없음 (겹쳐도 J로 유지)
                        jihun.append((j_nx, j_ny))
         
        move = move+1
bfs(maze, escape)

#bfs하고 나서 escape 리스트 확인하기.
#탈출할수있는경우 최솟값을 출력
if len(escape)>0:
    print(min(escape))
else:#0일때
    print("IMPOSSIBLE")
#print(escape)
