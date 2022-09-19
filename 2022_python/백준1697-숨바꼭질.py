from collections import deque
import math

#수빈/동생위치
N,K = map(int, input().split())

subin=deque()
#깊이
depth=0
#시작점 넣어주기
subin.append((N,depth))
#방문했던 숫자 넣어주기.
visit=[0]*100001

def bfs(subin, K,visit):
    while subin:
        p,d = subin.popleft()
        visit[p]=d#방문표시
        #1, -1, *2로 이동
        move=[1,-1,p]
        #방금 출력위치가 동생위치와 같다면
        if p ==K:
            return d
            break
        else:
            for i in range(3):
                n_p = p+move[i]
                #방문하지 않았었다면
                if (n_p > -1 and n_p < 100001) and visit[n_p] ==0:
                    #print(n_p)
                    subin.append((n_p,d+1))

result = bfs(subin,K,visit)
print(result)
#(n_p >=0 and
