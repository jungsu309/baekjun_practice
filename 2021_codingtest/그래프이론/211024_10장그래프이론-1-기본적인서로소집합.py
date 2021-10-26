#특정원소가 속한 집합 찾기
#여기서 parent<<는 리스트임.
def fine_parent(parent,x):
    #루트노드가 아니면, 루트노드를 찾을때까지 재귀호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

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
#부모정보리스트에 일단은 자기 자신으로 부모 설정
for i in range(1, v+1):
    parent[i] = i

#순서쌍 입력 받고 union 연산 해주기
for i in range(e):
    a, b = map(int, input().split())
    union_paren(parent, a, b)

#집합을 출력
print("각 원소가 속한 집합 : ", end = " ")
for i in range(1, v+1):
    print(find_parent(parent, i), end= " ")
print()

print('부모테이블 : ', end = " ")
for i in range(1, v+1):
    print(parent[i], end = " ")
