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


#정렬해보자 - 먼저 피고 먼저 지는거 위주로 먼저 정렬시켜보자.
flower_sort = sorted(flower,key =  lambda x: (x[0],x[1]))
print(flower_sort)

# 이날짜보다는 빨리 펴야한다
target = 301 #초기 설정에서 3/1에는 펴있어야 하기 때문.

