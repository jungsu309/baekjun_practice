#heapq써보기
import heapq
n, m = map(int, input().split())
#print(n,m)

card=list(map(int, input().split()))

Q=[]
for i in range(0,n):
    heapq.heappush(Q,card[i])#알아서 정렬됨
    
for i in range(0,m):#m회 반복
    #제일 작은거 두개 고르기->맨앞에 두개
    Q_0 = heapq.heappop(Q)
    Q_1 = heapq.heappop(Q)
    comb = Q_0 + Q_1 
    #값 바꾸기
    heapq.heappush(Q, comb)
    heapq.heappush(Q, comb)

print(sum(Q))
