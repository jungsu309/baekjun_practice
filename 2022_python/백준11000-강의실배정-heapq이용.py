#우선순위 큐
import heapq
from sys import stdin

#수업개수 N
N = int(stdin.readline())
timetable=[]
for i in range(0,N):
    timetable.append(list(map(int, stdin.readline().split())))
#print(timetable)

#정렬 :  빨리끝나고, 빨리 시작하는거 순서대로 정렬
timetable_sort = sorted(timetable, key=lambda x:(x[0],x[1]))
#print(timetable_sort)


Q=[]
#첫번째 요소의 끝나는시간. end_time과 유사
heapq.heappush(Q, timetable_sort[0][1])
#print(Q)

for i in range(1,N):#시간표 개수만큼
    #연달아 할 수 있을때
    if Q[0] <= timetable_sort[i][0]:
        #기존에 있던 값을 빼준다(교체해야하니까?)
        heapq.heappop(Q)
        heapq.heappush(Q,timetable_sort[i][1])
    #시간이 겹쳐서 같이 못들을때
    else:
        heapq.heappush(Q,timetable_sort[i][1])

#endtime를 이용해서 계속 돌면서 이어서 할 수 있을때 endtime를 교체해준다
# 이어서 못할때는 새로운 endtime를 등록해준다. endtime자체가 수업의 개수를 뜻한다!!!
print(len(Q))
