#2021.10.24 10장 그래프이론 -2- 팀 결성

#팀 합치기 연산
#같은팀 여부 확인 연산

#N : 노드수, M : 연산의 개수
N,M = map(int, input().split())


#부모노드 알아보기
def find_parent(parent, x):
    #parent[x]가 루트노드가 아닌경우
    if parent[x] != x:
        #재귀
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#합치기
def union_team(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #둘중에 작은게 부모가 됨
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


#parent 초기화 해주기
parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i


for i in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_team(parent, a,b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

    
