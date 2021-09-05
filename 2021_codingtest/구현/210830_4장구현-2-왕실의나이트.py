#20210830-4장 구현 2.왕실의 나이트
#상하좌우와 비슷한 방법으로 작성하였다.

#입력값
N = input()
x = int(ord(N[0])-ord('a')+1)#a=1, b=2->숫자로 변환
y = int(N[1])

#갈수있는 방법8가지?
dx = [2,2,-2,-2,-1,1,-1,1]
dy = [-1,1,-1,1,2,2,-2,-2]

#이동가능한 방향들 갯수 세기
count=0

for i in range(len(dx)):
    move_x = x + dx[i]
    move_y = y + dy[i]
    if move_x<1 or move_x>8 or move_y<1 or move_y>8:
        continue
    else:
        count = count+1

print(count)
