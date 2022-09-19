# 회의실 배정과 유사한거같다. 근데 날짜개념이 들어가있음..
#근데 날짜 개념이 딱히 필요없을지도 모른다?

N = int(input())

flower=[]

#날짜 계산이 어려우니, 월에다 100을 곱해주자.............
for i in range(0,N):
    
    array = list(map(int, input().split()))
    start = array[0]*100 + array[1]
    end = array[2]*100+array[3]
    flower.append([start,end])
print(flower)


#꽃이 피기 시작하는날 :  3/1보다 전에 피어야하고, 끝나는 날보다 빨라야한다.
#꽃이 지는날 : 늦어야 한다. 11/30 보다 늦게 져야 한다.


#정렬해보자 - 첫 시작을 위해
flower_sort = sorted(flower,key =  lambda x: (x[0],-x[1]))

print(flower_sort)

#시작날짜 구하기 - 첫날의 지는 날짜가 3월 이상이어야함

start_point=[]
cnt = 0
for i in range(0,N):
    if (flower_sort[i][1] >= 301) & (flower_sort[i][0] <= 301):
        start_point.append(flower_sort[i])
print(start_point)
#print("본인없는 list",flower_sort)

start_point = sorted(start_point, key=lambda x: -x[1])
start_point = start_point[0]
print(start_point)
#첫번째 꽃을 고르게 되는 시점
cnt = cnt+1

start_index = flower_sort.index(start_point)
del flower_sort[start_index]

print(flower_sort)



print("거지같은 포문 시작!")
#그 뒤부터 꼬리잡기로 해보자
for i in range(0, N-1):

    print("비교용")
    print("start",start_point)
    print("flower_sort",flower_sort[i])

    #시작하는 날이랑 비교
    #나중에 피는 꽃이랑 만나거나 겹쳐야함
    if (flower_sort[i][0] <= start_point[1]):        
        #끝나는 날도 서로 비교를 해야함 ex-(start)[4, 12, 6, 5], (next)[5, 2, 5, 31] 의 경우 [5, 2, 5, 31] 를 포함 시킬 이유가 없음. 
        if(flower_sort[i][1] >= start_point[1]):
            cnt = cnt+1
            start_point = flower_sort[i]
            print("체크포인트",start_point)
    #마지막날 11/30 을 넘어야한다. 11/30 이거나 12/1 이후여야 함.
    if (start_point[1] >= 1130) :
        print("break_point",start_point)
        break
print(cnt)
