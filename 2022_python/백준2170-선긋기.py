from sys import stdin
import heapq

#우선순위 큐 써보자.
N = int(input())
lines = []
for i in range(0,N):
    heapq.heappush(lines, tuple(map(int, stdin.readline().split())))
#힙이라서 바로 정렬이 된다.

#endpoint- 시작점 기준으로 초기화
endpoint = lines[0][0]
#제일 첫 시작점
startpoint = lines[0][0]

answer = 0
while len(lines) > 0:

    if endpoint >= lines[0][0]:#연결이 가능#
        #print("endpoint", endpoint, "lines[0][0]", lines[0][0])
        #endpoint update
        p = heapq.heappop(lines)
        if p[1] > endpoint:# endpoint를 갱신하는 경우
            endpoint = p[1]
        #else:# 완전 안에 쏙 들어오는 경우 - endpoint그대로 유지
        #print(endpoint)

    else: #연결이 불가능. 연결했을때까지의 값 정리 하고 연결 안되는 쌍을 기준으로 새로 시작
        answer = answer + (endpoint - startpoint)
        out = heapq.heappop(lines)
        #print(out)
        endpoint = out[1]
        startpoint = out[0]

#마지막 차이
answer = answer + (endpoint - startpoint)
print(answer)
