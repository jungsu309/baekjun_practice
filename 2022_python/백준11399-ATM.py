#N = 사람의 수
N = int(input())

#time = 각 사람이 인출에 걸리는 시간
time = list(map(int, input().split()))

#인출이 빨리 끝나는 사람부터 정렬 
time_sort = sorted(time)

time_sum=0
for i in range(0,N):
    time_sum = time_sum + (time_sort[i]*(N-i))
print(time_sum)
