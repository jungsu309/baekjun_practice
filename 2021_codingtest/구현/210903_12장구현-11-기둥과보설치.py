#20210903-12구현-11 기둥과 보 설치
#https://www.youtube.com/watch?v=_hVVk-frECw 설명 영상 보고 공부하였음

#전역변수로 기둥, 보 각각의 배열을 만들어줄거임.
pillar=[[]]
bar=[[]]

def checkpillar(x,y):
    #바닥이 0인 경우(맨 처음), 바로 밑에 기둥이 있는경우
    if y == 0 or pillar[x][y-1]:
        return True
    #보가 옆에 있는 경우(보는 스타트 지점이 바의 왼쪽이다.)
    if (x > 0 and bar[x-1][y]) or bar[x][y]:
        return True
    #두 if 문에 해당하지 않는 경우
    return False

def checkbar(x,y):
    #근처 아래에 기둥이 있는 경우(보는 가로 선이니까 기둥 두군데 중 한군데에 중 하나에 있으면 됨)
    if (y > 0 and pillar[x][y-1]) or (y > 0 and pillar[x+1][y-1]):
        return True
    #양 옆에 보가 있는 경우
    if (x > 0 and bar[x-1][y]) and bar[x+1][y]:
        return True
    #두 if 문에 해당하지 않는 경우
    return False

def candelete(x,y):
    #구조물은 좌우, 그리고 상단 과 상단의 좌우에 영향을 미칠 수 있음-> 최대 6군데에 영향을 미칠 수 있음..
    for i in range(x-1, x+2):#설명에서 x+1이니까 x+2로 하면되겠죠 라고 하는데-> range에서 마지막 값은 포함하지 않기 때문.
        for j in range(y, y+2):
            #기둥을 삭제 한 후 조건에 안맞게 되면
            if pillar[x][y] and checkpillar(i,j) == False:
                #삭제할 수 없는 상태인 것이다.
                return False
            #보를 삭제 한 후 조건에 안맞게 되면
            if bar[i][j] and checkbar(i,j) == False:
                #삭제할 수 없는 상태인 것이다.
                return False
    #그 외의 경우는 지워도 되는 상황인것.
    return True

def solution(m, build_frame):
    global pillar, bar

    #좌표의 모서리를 확인하는 이론을 사용하기 때문에  제공되는 2차원 배열보다 1칸씩 더 많아야 함.
    pillar = [[0 for _ in range(n+1)]for _ in range(n+1)]
    bar = [[0 for _ in range(n+1)]for _ in range(n+1)]

    for x,y,kind,cmd in build_frame:
        #기둥인경우
        if kind == 0:
            #설치하는 경우
            if cmd == 1:
                #설치 가능 유무 true-설치가능 false-설치불가능
                if checkpillar(x,y):
                    pillar[x][y] = 1
            #삭제하는 경우
            else:
                #먼저 삭제해보고
                pillar[x][y] = 0
                #삭제 가능한지 여부를 살피는데, 아닌경우 다시 복구하기
                if not candelete(x,y):
                    pillar[x][y] = 1
        #보인경우
        else:
            #설치하는 경우
            if cmd == 1:
                #설치 가능 유무 true-설치가능 false-설치불가능
                if checkbar(x,y):
                    bar[x][y] = 1
            #삭제하는 경우
            else:
                #먼저 삭제해보고
                bar[x][y] = 0
                #삭제 가능한지 여부를 살피는데, 아닌경우 다시 복구하기
                if not candelete(x,y):
                    bar[x][y] = 1
                
    answer=[]
    
#x오름차순 후 같으면 y오름차순 해서 정렬
    for x in range (n+1):
        for y in range(n+1):
            if pillar[x][y]:
                answer.append([x,y,0])
            if bar[x][y]:
                answer.append([x,y,1])
            
    return answer
