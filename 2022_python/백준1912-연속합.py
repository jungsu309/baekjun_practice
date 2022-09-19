n= int(input())

li = list(map(int, input().split()))
#print(li)

sumlist=[0]*(n+1)
#누적합 구하기
for i in range (1,n+1):
    sumlist[i] = sumlist[i-1] + li[i-1]
#print(sumlist)


max_num =-float("inf")

for i in range(1,n+1):
    min_num = min(sumlist[:i])
    if sumlist[i]-min_num > max_num:
        max_num = sumlist[i]-min_num

print(max_num)

