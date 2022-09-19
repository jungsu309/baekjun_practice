from sys import stdin
from collections import deque
#테스트 케이스 개수2 가로 M 세로 N, 배추 개수 K
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue, graph):
    while queue:
        p1, p2 = queue.popleft()
        graph[p1][p2]=2#방문 표시
        #사방 확인
        for i in range(4):
            n_p1 = p1 + dx[i]
            n_p2 = p2 + dy[i]
            if n_p1 >-1 and n_p1<N and n_p2 >-1 and n_p2 <M and graph[n_p1][n_p2] ==1:
                graph[n_p1][n_p2]=2#방문 표시
                queue.append((n_p1,n_p2))

                
for i in range(T):
    M, N, K = map(int, input().split())
    position=[]

    soil = [[0]*M for i in range(N)]
    #print(soil)
    
    for j in range(K):
        position.append(list(map(int, stdin.readline().split())))
    Q=deque()

    #input으로 받은 list를 graph로 표현하기.
    for p in position:
        soil[p[1]][p[0]] = 1
    #print(soil)

    count=0

    for n in range (N):
        for m in range (M):
            if soil[n][m] ==1:
                #print("1인곳",n,",",m)
                count = count+1
                Q.append((n,m))
                bfs(Q, soil)
    #print(soil)
    print(count)


