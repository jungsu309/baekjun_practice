from sys import stdin
import copy
import sys

sys.setrecursionlimit(100000)
N = int(input())

graph_original=[]
for i in range(N):
    graph_original.append(list(map(int, stdin.readline().split())))
#print(graph_original)
max_hieght = max(map(max, graph_original))

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

def dfs (x,y,graph):
    graph[x][y] =0
    #현재 위치 필요
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>-1 and nx<N and ny>-1 and ny<N and graph[nx][ny] != 0:
            #print("nx,ny",nx, ny)
            #직전에 들렸던곳 = 방문처리
            graph[nx][ny] =0
            dfs(nx, ny,graph)
    #cnt = cnt+1      




#높이가 0~100인데 제일 높은 봉우리 이후 값은 어차피 다 잠겨서 계속 0나옴-> 반복문 횟수 조절필요
cntlist=[0]*(max_hieght+1)
for rain in range (0,max_hieght+1):
    graph = copy.deepcopy(graph_original)
    cnt =0
    #i보다 작은 숫자들은 전부 0으로 만든다..?
    for k in range(N):
        for j in range(N):
            if graph_original[k][j] <= rain:
                graph[k][j] =0
                #print(graph_original)
                #print(graph)

    #print("안잠긴 땅",graph)
    #이상태에서 dfs 해보기
    for k in range(N):
        for j in range(N):
            if graph[k][j] !=0:
                #print("k,j",k,j)
                #print(graph)
                dfs(k,j,graph)
                cnt = cnt+1
    cntlist[rain] =cnt
#print(cntlist)
print(max(cntlist))            
