from collections import deque
from sys import stdin
import copy
import sys
sys.setrecursionlimit(100000)

N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph=[]
for n in range(N):
    graph.append(list(map(int, stdin.readline().split())))

#print(graph)

#dfs 로 육지 표시 2부터~n까지 (1은 겹쳐서)
def dfs(x,y,g):
    graph[x][y] = g#방문겸 육지 표시
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>-1 and nx<N and ny>-1 and ny<N and graph[nx][ny]==1:
            dfs(nx,ny,ground)#같은 육지일때는 그대로 감
            

ground=1
for n in range(N):
    for m in range(N):
        if graph[n][m] ==1:
            ground = ground+1
            dfs(n,m,ground)#2부터 시작해서 1씩 늘어나게됨
#print(graph)


#가장 근처에서 다른 숫자 찾기-> bfs(최단거리라서)
#육지 개수 = ground-1
#print(ground-1)


length=[]#육지마다 1개씩 길이저장-bfs라 제일 빨리 들어가는게 최소값일것이다..
queue_list=[]

def bfs(queue,matrix):
    #length_g = []#섬마다의 최소 길이를 알고싶어서.
    flag = False
    #print(queue)#맨처음 큐
    while queue:
        #print(len(queue))
        x,y,c,g = queue.popleft()#c=다리길이, g = 내 땅의 숫자
        #queue_list.append((x,y,c,g))
        #print("큐에서 탈출",x,y,c,g)
        #print(g)
        #print(matrix)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #다른 육지를 찾으러 감
            #print("주변 살피기", nx,ny)
            if nx>-1 and nx<N and ny>-1 and ny<N:
                #육지 늘려가면서 찾기
                if matrix[nx][ny]==0:
                    #print("출발지", x,y, "나아갈 수 있는곳.", nx,ny,"이동거리(c)",c)
                    matrix[nx][ny] =g#방문처리
                    queue.append((nx,ny,c+1,g))#다리 길이 늘려줌
                    #print("큐에 추가", nx, ny,c+1,g)
                elif matrix[nx][ny] != g:#지금 내땅도 아니고 0도 아님->다른 육지 찾음
                    length.append(c)
                    #print("다른육지 발견-x,y",x,y,"matrix[nx][ny] ,g,c",g,c,"nx,ny:" ,nx,ny)
                    #print("x,y의 c",c,"matrix[nx][ny]의 c", c)#어쨋든 같


                    #print("x,y를 찾기")
                    #print(queue)
                    for q in queue:
                        if (nx == q[0]) and (ny == q[1]):
                            #print("포함된거라도 찾을수있다.")
                            #print(q)
                            #length.append(q[2]+c)
                            answer = q[2]+c
                    flag = True#첫번째로 다른육지 발견->제일빨리찾은애= 제일 가까운애
                    break
        if flag == True:
            break

    print(answer)



Q = deque()#큐도 초기화
Q_list=[]
#print("graph와 동일한 graph_copy", graph_copy)
for n in range(N):
    for m in range(N):
        #육지가 있을때
        if graph[n][m] != 0:#경계에 있는것들
            #print("g먼저 찾기", g)
            for i in range(4):
                nx = n + dx[i]
                ny = m + dy[i]
                if nx>-1 and nx<N and ny>-1 and ny<N and graph[nx][ny] ==0:
                    Q_list.append((n,m,0,graph[n][m]))#초기에 섬의 가장자리에 있는애들 전부 넣어주기->겹치네;;
#set으로 중복 없애기
#print(Q_list)
Q_list=set(Q_list)
#print(Q_list)
#print(len(Q_list))
for q in Q_list:
    Q.append(q)
bfs(Q,graph)



#print(min(length))






    
