#20210906-5장 DFS/BFS 3 음료수 얼려 먹기
#상하좌우가 붙어있는경우 하나로 취급

#리스트를 노드로 바꾼다음에 생각해보기 이차원 배열로 만드는게 편할듯. N*M 꽉차있어서.

#N:세로길이  M:가로길이
N,M = map(int, input().split())

array_2=[]


for n in range(N):
   array_2.append(list(map(int, input())))

#print(array_2)->세로n 가로m->[n][m]순서
#상하좌우 살펴보기 DFS써보기

#x:세로 y:가로
def dfs(graph, x,y):
    #칸을 넘어가는 경우
    if x<0 or x>=N or y<0 or y>=M:
        return False
    #빈공간인 경우
    if graph[x][y] == 0:
        #한번 방문했으니까 다시 방문하는것을 방지
        graph[x][y] = 2
        #상하좌우 살피기
        dfs(graph, x-1,y)
        dfs(graph, x,y-1)
        dfs(graph, x+1,y)
        dfs(graph, x,y+1)
        return True
    #주변에 더이상 0인 곳이 없을때
    return False

cnt=0
for i in range(N):
    for j in range(M):
        if dfs(array_2, i,j):
            cnt = cnt+1

print(cnt)
