#로프 개수 N
N = int(input())

#각로프가 받을 수 있는 최대하중
weight = []
for i in range(0,N):
    weight.append(int(input()))
#print(weight)

#한번 정렬이 필요하다.내 방법은 제일 작은 로프가 앞에 있는 기준이기때문임.
weight = sorted(weight)#오름차순 인듯

#모든 경우의 수를 구한다음에 최댓값을 구해보자.
all_weight=[]
for i in range(0,N):
    all_weight.append(weight[i]*(N-i))
#print(all_weight)

#최대중량 = max
print(max(all_weight))
