#N= 회의개수

N = int(input())

timetable = []
for i in range(0,N):
    timetable.append(list(map(int, input().split())))
print(timetable)#2차원 배열

#가장 많이 우겨넣으려면 차이 적은거 위주로 재정렬 시켜보자
#둘 값을 뺀 값으로 정렬해보기

#timetable_sort =[]
#min_distance = timetable[0][1] - timetable[0][0]#임시 최소값
#for i in range (0, N):
#    distance = timetable[i][1] - timetable[i][0] 
#    if min_distance > distance:
#        min_distance = distance

#sorted 함수에 조건을 직접 넣어보자. lambda식이용할수있다.

#sorted_list = sorted(timetable, key = lambda x : x[1]-x[0])
#print(sorted_list)


#차이로 접근하지말고, 끝시간, 시작시간으로 접근하기..

sort_list = sorted(timetable, key=lambda x:x[0])
print(sort_list)
sort_list = sorted(sort_list, key=lambda x:x[1])
print(sort_list)

#위랑 아래랑 같음.
sort_list2 = sorted(timetable, key=lambda x:(x[1],x[0]))
print(sort_list2)

#꼬리잡기 식으로 다음 회의시간 선택.
#첫 회의는 제일 앞에 나와있는 시간으로 시작
cnt = 0
end = sort_list[0][1]#이 시간에 맞춰서 다음 회의 찾자
cnt=cnt+1
for i in range(1,N):
    if sort_list[i][0]>= end:
        cnt = cnt+1
        end = sort_list[i][1]
print(cnt)


