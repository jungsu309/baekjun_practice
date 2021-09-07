#20210906_13장 DFS/BFS 15번 특정거리의 도시찾기

from collections import deque
#N:도시개수 M:도로개수 K:거리정보 X:출발도시번
N, M, K, X = map(int, input().split())

#방향이 있고 갈수있는 길이 정해져있으니까 인접리스트를 쓰는게 좋아보임- 구글링참
graph={}
for m in range(M):
    x, y = map(int, input().split())
    if x not in graph.keys():
        graph[x] = set([y])
    else:
        graph[x].add(y)

#길 스타트가 아닌애들(출발지가 아닌곳들)도 0넣어주기.
for n in range(1,N+1):
    if n not in graph.keys():
        graph[n] = None

#for i in graph[1]:
#    print(i)
#print(graph)
#print(graph[1])
#print(len(graph[3]))

#방문을 표시할 배열 준비. K보다 빠르게 갈수 있는곳은 K로 취급 안해서 표시해야함.
#N+1로 하는 이유는 도시가 1부터 시작해서. 아래에서 i를 i+1로 해도되지만 그러면 도시 이름도 꼬이고 헷갈릴 수 있어서 그냥 0포함해서 1개
#더 많게 구성하였다
visit_array=[False]*(N+1)
result=[]

#dfs가 잘안되서 bfs써보려고 한다.
queue = deque()

queue.append((X,0))
while queue:
    start_city,moves = queue.popleft()
    #인접리스트에 있는곳 일단 다 가보기
    if graph[start_city] is not None and moves < K:
        for i in graph[start_city]:
            #방문한적이 없는곳으로. 
            #print(visit_array)
            if visit_array[i]==False:
                visit_array[i]=True
                queue.append((i,moves+1))
    elif moves == K:
        result.append(start_city)


if len(result) == 0:
    print("-1")
else:
    #한줄에 하나씩 오름차순으로.
    result.sort()
    for r in result:
        print(r)
        
            




