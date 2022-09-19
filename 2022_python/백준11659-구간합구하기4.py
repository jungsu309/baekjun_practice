#import copy
N, M = map(int,input().split())

N_list = list(map(int, input().split()))#0~N-1까지 N개

i_j=[]
for m in range(M):
    i_j.append(list(map(int,input().split())))

#print(N_list, i_j)
#1부터 N까지의 합을 전부 구해놓는다.
sum_list = [0]*(N+1)#0번째 인덱스 비워놀거라서

for i in range(1,N+1):#N개
    sum_list[i] = sum_list[i-1] + N_list[i-1]#얘는 0부터 들어있어서..

#print(sum_list[:N+1])

for k in i_j:
    i=k[0]
    j=k[1]
    #print(i,j)
    print(sum_list[j]-sum_list[i-1])
    
