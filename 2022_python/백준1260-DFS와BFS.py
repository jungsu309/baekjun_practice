from collections import deque

N,M,V=map(int, input().split())

graph= []
visit_dfs=[0]*(N+1)
visit_bfs=[0]*(N+1)


def dfs(graph, v, visit):
    #첫번째로 입력받은 V부터 시작!
    visit[v]=1
    print(v, end=' ')
    #그래프로 접근
    for i in range(N+1):
        #출발노드(v)~도착노드(0~N+1까지)돌리면서 연결된 것 찾음!(1여부) 그리고 방문한적이 없어야함!
        if graph[v][i]==1 and visit[i]==0:#조건 자체는 bfs와 동일
            #bfs의 경우 앞에거먼저 하고 나중거는 뒤에 쌓이는 형식이고
            #dfs의 경우 발견하는 즉시 거기서 한번 더 반복하는 형식
            dfs(graph, i, visit)
    
def bfs (graph, v, visit):
    #처음으로 입력받은 V부터 시작
    queue=deque()
    queue.append(V)
    visit[v]=1
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        #graph로 접근
        for i in range(N+1):#작은거부터 돌기때문에 (0->N+1까지) 무조건 노드숫자가작은거부터 출력된다.
            #출발노드(v)~도착노드(0~N+1) 에서 연결된 것 찾기(1로 표시되어있는게 서로 연결된것)
            #도착노드가 한번도 들려진적없으면!!
            if graph[v][i] ==1 and visit[i]==0:
                queue.append(i)#도착노드를 추가. 이제 다음부터 이거 차례대로 꺼내서 돌것.
                visit[i] = 1

    
#노드 개수만큼 정사각형모양의 그래프를 미리 만들어주자.
graph = [[0]*(N+1) for i in range (N+1)]
for i in range (M):
    a, b = map(int,input().split())
    #양방향 노드니까.. 양쪽다 1로 표시해주자.
    graph[a][b]=graph[b][a] = 1
#print(graph)

#dsf
dfs(graph, V,visit_dfs)

print()
##bfs

bfs(graph,V,visit_bfs)





