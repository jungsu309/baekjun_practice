#특정원소가 속한 집합 찾기
#여기서 parent<<는 리스트임.
def fine_parent(parent,x):
    #루트노드가 아니면, 루트노드를 찾을때까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #원소가 작은게 부모가 됨
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선의 개수 받기
v,e = map(int, input().split())
#부모정보 리스트 만들기
parent=[0]*(v+1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0

#부모테이블 초기화. 자기자신으로
for i in range(1, v+1):
    parent[i] = i

#사용자로부터 데이터 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    #비용이 적은거 기준 오름차순 나열해야해서 첫 원소를 비용으로
    edges.append((cost, a, b))

edges.sort()

#간선을 하나씩 확인하기
for edge in edges:
    #사이클 판단했는데 사이클이 안이루어지면
    if find_parent(parent, a) != find_parent(parent, b):
        #연결하기
        union_parent(parent, a,b)
        result += cost

print(result)    
    
    
