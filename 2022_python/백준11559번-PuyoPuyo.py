import sys
#sys.setrecursionlimit(100000)

#12행 6열
field=[]
#이동
dx=[-1,1,0,0]
dy=[0,0,-1,1]

row = 12
col = 6
for i in range(row):
    field.append(list(map(str, input())))
#print(field)


def dfs(graph,visit,x,y, li):
    global cnt_4
    now = graph[x][y]
    li.append((x,y))
    visit[x][y] = 1#방문표시
    #print("연결된 뿌요")
    cnt_4= cnt_4+1#연속 뿌요 갯수
    #print(c)
    #사방을 둘러본다
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>-1 and nx<row and ny>-1 and ny<col and graph[nx][ny] == now and visit[nx][ny] ==0:#같은 알파벳 찾기
            li.append((nx,ny))
            
            dfs(graph, visit,nx, ny, li)
            #print(cnt_4)
    #print("출력 직전",cnt_4)

    return cnt_4


def find_bottom(x,y):
    bottom = -1
    for i in range (x, row):#0은 꼭대기라.. 그냥 .으로 채워줄 수 밖에없다.
         if field[i][y] =='.':
             bottom = i
    return bottom
    

cnt = 0
while True:
    flag = 0
    visit = [[0] *(col) for _ in range (row) ] #초기화..
    #print(field)
    #print(visit)
    for x in range(row):
        for y in range(col):
            if visit[x][y] ==0 and (field[x][y] == 'P' or field[x][y] == 'R' or field[x][y] == 'Y' or field[x][y] == 'B' or field[x][y] == 'G'):#아직 방문 안했고#색 찾기
                cnt_4=0
                puyolist=[]
                gather = dfs(field,visit, x, y, puyolist)

                #print("연결뿌요",gather)
                puyolist = set(puyolist)
                #print(puyolist)
                if gather>=4:
                    flag = 1
                    for puyo in puyolist:
                        #print(puyo[0],puyo[1])#4개이상출력되야함
                        field[puyo[0]][puyo[1]] = '.'#4개 이상일때 터트리고 .으로 표현
    if flag == 0:#4개 묶여진적이 없다
        #print("탈출시점")
        break#while문 탈출

    
    #print(visit)
    cnt = cnt+1
    #print(cnt)
    
    for y in range(0,col):
        for x in range(row-2, -1, -1):
            bottom = -1
            if field[x][y] !='.':
                bottom = find_bottom(x,y)
            #떠있는거 아래로내리기 -> 알파벳 밑에 .이 있는경우 !
            if bottom !=-1:#알파벳을 옮기기
                field[bottom][y] = field[x][y]#지금알파벳으로바꾸기
                field[x][y]='.'# 바꾸고나서는 점으로 바꾸기

print(cnt)

                
