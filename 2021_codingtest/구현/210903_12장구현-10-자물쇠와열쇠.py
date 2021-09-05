#20210830-12장 구현 10 자물쇠와 열쇠

#key = MxM , lock = NxN lock에 꼭 맞으면 됨. key는 튀어나가도 상관없음
#N>M 자물쇠가 같거나 크다

#key와 lock은 2차원 배열 형태

#답지 보고 공부했다
#https://www.youtube.com/watch?v=RrWnBaflV2o 풀이 동영상
#자물쇠를 기준으로 키를 계속 움직이는 방법 이용.
#돌기가 겹쳤을 때 1+1=2, 딱 맞물렸을때 1+0 =1 둘다 비었을 때 0+0 << 이 방법 이용. 4방향 다 돌려보고 키 이동시키기.
#모든 경우의 수를 해보는 방법으로 풀기.

#먼저 lock과 key를 배치할 0으로 이루어 진 큰 이차원 배열 필요. 겹치게 배치 가능한 크기로 만든다.
#마무리-> 자물쇠 부분이 모두 1인 상황.
def match(arr, key, rot, r, c):
    n = len(key)
    for i in range(n):
        for j in range(n):
            #key 그대로
            if rot ==0:
                #lock 이 있는 경우 겹치면 2 가 되게 계산해야하니까 기존거에 더하는 식으로 진
                arr[offset + i][offset + j] += key[i][j]
            #시계방향으로 돌리기
            else if rot==1:
                arr[offset + i][offset + j] += key[n-1-j][i]
            else if rot==2:
                arr[offset + i][offset + j] += key[n-1-i][n-1-j]
            else:
                arr[offset + i][offset + j] += key[j][n-1-i]

def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            #배열에서의 자물쇠에 해당하는 부분 확인하기
            #1이 아니면 
            if arr[offset + i][offset + j]!= 1:
                return False
    #if문을 한번도 안탄것->전부 1인경
    return True
            
def solution(key, lock):
    #빈 2차원 배열에 맨처음에 lock을 배치하는 위치. 가운데다가 딱 놔야함.
    offset = len(key)-1

    #key가 움직이는 범위. 마지노선 한칸 겹칠때까지 내릴 수 있음. key, lock모두 정사각형이라 행열 크기가 같다.
    for row in range(offset + len(lock)):
        for col in range (offset + len(lock)):
            #4방향으로 돌릴거임.
            for rot in range(4):
                #key와 lock을 올릴 0으로 된 큰 이차원 배열 설정. 돌릴때마다 달라지니까 여기 아래에 매번
                #만들어줘야하는듯하다. 58은 key 최대 20, lock 최대 20이라서 가능한 제일 큰 배열은 58*58이 됨.
                arr = [[0 for _ in range(58)]for _ in range(58)]#2차원 배열 0으로 초기화

                #0으로 초기화 된 2차원배열 가운데 lock배치
                for i in range (len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]

                # 돌려서 껴넣는 코드. 
                match(arr, key, rot, r, c)

                #lock 부분이 전부 1인지 확인하는 코드
                if check(arr, offset, len(lock)):# 다 1이면 true, 아니면 false
                    return True
                        
    #해당하는 정답이 없는 경우
    return False
