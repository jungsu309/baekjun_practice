INF = int(1e9)

n = int(input())
m = int(input())

#N*N이차원리스트를 inf로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range (1, n+1):
    for b in range(1, n+1):
        #자기자신인경우
        if a == b:
            graph[a][b] = 0

#for m in range(m):
#    a,b,c = map(int, input().split())
#    graph[a][b] = c

#위에처럼 그냥 하는 경우 덮어쓰기가되버리는 경우 발생.
#방문이력이 있는 경우 기존거랑 비교해주는 과정이 필요할듯하다.

for m in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] =c
    else:
        continue

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('0' , end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
