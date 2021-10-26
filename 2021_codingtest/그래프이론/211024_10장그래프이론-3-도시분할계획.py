#2021.10.24 10장 그래프이론 -3- 도시분할계획

#하나의 마을을 두개로 분리하기. 마을에는 집이 하나 이상있어야함. 그리고 최소경로여야함.
#아이디어-> 최소신장그래프(크루스칼) 그리고, 간선의 크기가 제일 큰 것을 제거하게 되면 마을이 분리가될것.
#연결하는 길이 여러개면 제거가능

#N, M
N, M = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

#부모테이블 초기화
parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

#간선정보를 담기
edgds = []
#유지비의 합
result = 0

#사용자에게 입력 받기
for i in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
#간선이 제일 큰 경우 필요한 변수
max_edge = 0

for edge in edges:
    C, A, B = edge# edge가 (C, A, B) 구조이므로 여기서 다시 변수에 도로 담아준다.
    #일단 사이클이 없어야함. 부모가 다르면 사이클x
    if find_parent(parent, A) != find_parent(parent, B):
        #연결시켜준다.
        union_parent(parent, A, B)
        result += C
        #어차피 edge가 작은거부터 큰거순으로 가기때문에 마지막 edge의 C가 제일 큰 비용임. 이 식으로 하면 어차피 남는건 마지막 C.
        max_edge = C

print(result-max_edge)

    
