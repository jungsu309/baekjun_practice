import heapq#heapq를 이용하여 개선하기.
import sys
input = sys.stdin.readline
INF = int(1e9)

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

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

#위에까지는 동일하게 초기화

def dijkstra(start):
    q=[]
    #시작노드로 가기위한 최단경로는 0으로 설정하기
    heapq.heappush(q,(0,start))
    disance[start]=0

    #큐가 빌때까지 계속 실행
    while q:
        #최단거리가 짧은 노드 꺼내기. 우선순위큐니까 그냥 꺼내면 됨
        dist, now = heapq.heappop(q)
        #이미 처리된 적이있는 노드라면 무시.
        if distance[now] < dist:
            continue
        for i in graph[now]:#[0] : 도착노드, [1]: 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
dijkstra(start)

#출력하기
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
