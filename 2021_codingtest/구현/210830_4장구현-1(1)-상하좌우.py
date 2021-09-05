#20210830-4장 그리디 예제문제 1) 상하좌우

#N*N의 정사각형에서, LRUD 명령어를 입력하여 도착지점을 출력하기.- 공간 밖은 무시하는 방법으로.
#시뮬레이션 형 문제. 한단계한단계 이동시키면 된다.

#이런 시뮬레이션 형식 문제에 익숙하지 않기때문에 답지를 토대로 작성해보았다.


#N*N틀
N = int(input())
#첫 시작 위치(1,1)
x,y=1,1

#사용자의 LRUD입력을 받음
plans = input().split()#리스트에 들어감.

#LRUD 에 따른 이동방향 매칭. 순서 맞춰줘야 함. 왜냐면 인덱스번호로 접근하기 때문.
move=['L','R','U','D']
#문제에서 나온대로 지정
dx=[0,0,1,-1]#세로
dy = [-1,1,0,0]#가로


for step in plans:#L R U D 가 step에 들어감
    for i in range (len(move)):#0~3의 인덱스 숫자가 들어감
        if step == move[i]:
            move_x = x + dx[i]
            move_y = y + dy[i]
    #move_x가 범위를 넘어서면 해당 작업 스킵
    if move_x<1 or move_x>N or move_y<1 or move_y>N:
        #현재위치 업데이트 하지 않음
        continue

    #새로운 위치로 업데이트
    x = move_x
    y = move_y

#모든 plans을 수행한 후 위치 출력
print(x,y)
            
