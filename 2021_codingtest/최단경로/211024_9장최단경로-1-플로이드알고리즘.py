INF = int(1e9)

#노드의 개수 간선의 개수 입력받기
n = int(input())
m = int(input())

#2차원 리스트 만들기. 일단 먼저 다 inf로 초기화해주기(연결안된애들은 다 inf니까)
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기자신->자기자신 경로는 0으로 설정. (대각선에 위치한애들)
for a in range(1, n+1):
    for b in range(1, n+1):
        if a== b:
            graph[a][b] =0

#각 간선의 정보를 입력하기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

#점화식을 통한 다이나믹프로그래밍이용하여 플로이드 구현
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#결과출력
for a in range(1, n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()#엔터
