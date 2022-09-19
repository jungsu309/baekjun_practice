from sys import stdin
import sys

sys.setrecursionlimit(3000000)

#n = 세로, m = 가로
n, m = map(int, input().split())

graph=[]
for i in range(0,n):
    graph.append(list(map(int, stdin.readline().split())))
    
#print(graph)
size = 0
#dfs
#x,y는 graph에서의 좌표로 보면 된다.
def dfs(x, y):
    global size
    #범위 조절
    if x <= -1 or x >= n or y<= -1 or y >= m:
        #갈곳이 더이상 없는 상태
        return False #함수니까 return써준다. 더이상 갈 데 없으니까 다른 곳에서 새로 찾아보기위해
    
    if graph[x][y] ==1:
        graph[x][y] = 0#방문했던데를 다시 방문하지 않게 하기 위해서!
        size = size+1
        
        #네방향 검사
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True # 1이 있는 지점 확인 완료 했다는 표시
    #그외의 경우
    return False

cnt = 0
sizelist=[]
for i in range(0,n):
    for j in range(0,m):
        if dfs(i,j) == True:#1찾은 경우
            cnt = cnt+1
            sizelist.append(size)
            #다른지점 체크하려면 다시 초기화해줘야한다.
            size = 0
            
if cnt ==0:
    print(0)
    print(0)

else:
    print(cnt)
    print(max(sizelist))
