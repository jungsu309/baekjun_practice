import sys
#빠른 input을 위함
input = sys.stdin.readline
INF = int(1e9)#무한을 의미하는 값

#노드의 개수와 간선의 개수
n, m = map(int, input().split())
#시작의 노드 (이때 노드는 1부터 시작하는 정수라고 생각)
start = int(input())

#각 노드에 연결되어있는 노드에 대한 정보를 담기
#노드간의 연결관계를 담는 리스트 만들기
graph = [[] for i in range(n+1)]#2중리스트

#방문했는지 체크하는 리스트 만들기
visited =[False]*(n+1)

#최단거리 테이블 . 맨처음은 무한대로 초기화
distance = [INF] * (n+1)

#간선 정보(거리정보)를 입력 받기
for _ in range(m):
    #a ->b 노드로 가는데 걸리는 비용(거리) c
    a,b,c = map(list, input().split())
    graph[a].append((b,c))#노드의 정보를 담기
    

#방문하지 않은 노드중에서 최단거리가 가장 짧은 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0#최단거리가 가장짧은 노드(그냥 일단 임시로 0으로 초기화해준것 뿐.)
    for i in range(1, n+1):
        #distance에서의 길이가 minvalue보다 작으면서 방문 안한경우
        if distance[i] < min_value and not visited[i]:
            #최소값 갱신
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start]=0#처음 거리는 0이니까.
    visited[start] =True# 첫번째 노드 방문처리해줌.

    for j in graph[start]:#첫 시작점 -> graph 모습 : 시작 노드 번째에 도착노드랑 거리 있음. 도착노드가 0번째 , 거리가 1번째 자리에 위치
        distatnce[j[0]] = j[1]#도착노드의 최단거리 그래프에 해당 거리를 넣어주기

    for i in range(n-1):
        #현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리해주기.
        now = get_smallest_node()#가장짧은 노드 번호를 획득
        visited[now] = True

        #지금 현재노드와 연결된 다른 노드들 확인하기
        for j in graph[now]: #j[0] = 도착노드 j[1] = 거리
            cost = distance[now] + j[1]
            #도착노드로 가기위해 필요한 거리가 경유해서 가는 경우가 더 짧을경우(cost:경유해가는방법) distance 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost

#다익스트라 실행
dijkstra(start)

#모든 노드로 가기위한 최단거리를 출력
for i in range(1, n+1):
    #갈수없는경우. INF인경우 출력방법
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

#시간복잡도 O(V^2)임
#노드및 간선이 많은경우 (10000개 정도)일때는 개선된 다익스트라알고리즘 사용해야한다.
