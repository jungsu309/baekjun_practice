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

#꼬리잡기로 생각해보기
answer = 0

#수업 수 말고 강의실 개수가 필요..
end_time = 0
i = 0
pop_count = 0
#초기 세팅-pop하기 전 모습 유지- 해당 step의 원본.
timetable_original=timetable_sort[:]
while True :
    if end_time <= timetable_original[i][0]:#pop한거로 하면 자리가 무너져서. 복사본으로 비교
        end_time = timetable_original[i][1]
        #print("pop 될 요소",timetable_original[i])
        
        timetable_sort.pop(i-pop_count)
        pop_count = pop_count+1
        #print("pop_count",pop_count)
    #else:# 출력용
        #print("시간이 겹쳐서 안될때!", i, timetable_original[i])
    i = i+1
    #print(i)
    #print("다 돌기 전까지 (i가 초기화 되기 전까지) 바뀌면안되는 original",timetable_original)
    #한바퀴 돌았을 때
    if i == len(timetable_original):
        #한바퀴 돌았으니 현재 list업데이트
        timetable_original = timetable_sort[:]
        #print("pop한 후 상태 ",timetable_original, len(timetable_original))

        #한바퀴 돌았을때 어쨋든든 1 증가
        answer = answer + 1
        
        #강의가 남아있는 경우
        if len(timetable_original) !=0:
            #처음부터 다시 돌려야하니까 i와 end_time를 초기화. + popcount도 초기화
            i=0
            end_time = 0
            pop_count=0
        #남은 강의가 없는경우. 멈추기
        if len(timetable_original) ==0:
            break

print(answer)
