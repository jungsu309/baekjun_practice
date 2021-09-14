#20210911- 14장 정렬 25 카드 정렬하기

#카드 비교할때 10 20 40 있으면 작은거끼리 먼저 하고 10+20 그 다음 30 +40 하는게 좋다
# 10 10 40 인 경우 10+10 +20+40으로 80 10+40+50+10= 110
#작은거 먼저 하고 큰거 하는게 이득이다.

N =  int(input())
array=[]
for n in range (N):
    num = int(input())
    array.append(num)

array.sort()
print(array)

mid_sum=array[0]
total_sum=0
for i in range(1,len(array)):
    mid_sum = mid_sum + array[i]
    total_sum = total_sum + mid_sum

print(total_sum)
