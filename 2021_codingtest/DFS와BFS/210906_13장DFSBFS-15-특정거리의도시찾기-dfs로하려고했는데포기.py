#20210906_13장 DFS/BFS 15번 특정거리의 도시찾기


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
        graph[n] = set([0])

#for i in graph[1]:
#    print(i)
#print(graph)
#print(graph[1])
#print(graph[3])
#시작점 : graph[X] -> 그리고 한번더 타는법 graph[graph[X]]...<< 재귀 써보자
cnt=0

#거리를 표시할 배열 준비
visit_array=[0]*N

def dfs(start_point):
    #갈길이 없으면서 distance가 0이 아닌경우
    if graph[start_point] == 0 and distance > 0:
        return False

    else:
        #인접리스트에 있는거만큼 다 해보기
        for i in graph[start_point]:
            visit_array[start_point] = visit_array[start_point]+1
            dfs(i)



if dfs(X):
    print(visit_array.index(K))
else:
    print("-1")


