from collections import deque

#노드의 개수와 간선의 수 받기
v, e = map(int, input().split())

#진입차수 일단 전부 0으로 초기화
indegree = [0]*(v+1)

#간선 정보를 담고있는 연결리스트 초기화
graph = [[] for i in range(v+1)]

#간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)#a->b로 이동할때의 간선 정보 넣기
    #화살표를 받는쪽에서의 진입차수 증가
    indegree[b] += 1

#위상정렬함수
def topology_sort():
    result=[]#수행결과 (순서)를 담아줄리스트
    q = deque()

    #처음시작할때, 진입차수가 0인거부터
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    #큐가 빌때까지 반복
    while q:
        #큐에서 하나 빼기(진입차수가 0인걸 빼는거임)
        now = q.popleft()
        result.append(now)
        #해당 노드와 연결된 애들 전부 indegree -1시켜줌
        for i in graph[now]:#i에는 원소들이 들어가있음 1->4에서 now가 1이면 i가 4 이런식
            indegree[i] -= 1
            #새로 진입차수가 0이 되는애들을 큐에 넣음
            if indegree[i] ==0:
                q.append(i)
                #큐가 빌때까지 반복

        for i in result:
            print(i, end=" ")
topology_sort()
            
