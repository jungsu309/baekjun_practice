#20210830-4장 구현- 3게임개발

#지금 방향 기준으로 왼쪽부터 시작
#갈곳이있으면 왼쪽으로 전진 갈곳 없으면 다시 한번더 왼쪽으로.
#네방향이 모두 갈수없는 길이면 한칸 뒤로 되돌아간다.
#뒤쪽도 바다면 게임 끝.
#맵 외곽은 항상 바다로 .

#맵 크기-세로 N, 가로M
N,M = map(int, input().split())
#맵 모양-2차원 배열?
array=[]
for i in range(N):
    array.append(list(map(int, input().split())))

#현재 위치..?
print(N,M)

#북동남서...방향이라는데 이해가 잘안된다...왜 북인데 -1 이
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#이해하기 어렵다...
def turn_left():
    global direction
    direction = direction -1
    if direction == -1:
        direction=3

count=1
turn_time=0
while True:
    #왼쪽으로 한번씩
    turn_left()
    nx = x + dx[direction]#회전하
    ny = y + dy[direction]


#그냥 모르겠다 ㄷㄷㄷㄷㄷㄷㄷ
    
