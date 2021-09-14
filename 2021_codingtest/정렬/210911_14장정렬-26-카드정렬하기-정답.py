import sys
# sys.stdin = open('input.txt')
import heapq
lis = []
n = int(sys.stdin.readline().strip())
while n:
    n-=1
    tmp = int(sys.stdin.readline().strip())
    heapq.heappush(lis, tmp)
answer=0 # if len(lis)==1 -> no comparision
while len(lis)>1:
    a=heapq.heappop(lis)
    b=heapq.heappop(lis)
    answer+=(a+b)
    heapq.heappush(lis, a+b)

sys.stdout.write(str(answer))

#출처: https://joey09.tistory.com/125 [joie de vivre]
