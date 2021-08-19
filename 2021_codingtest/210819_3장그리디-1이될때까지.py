#그리디 실전문제 - 1이 될 때까지
#2021.08.19

#N-어떤 수, K-나누는수
N,K = map(int, input().split())

count=0
#나눠지는 형태로 바꿔주고 나누기를 반복하기
while(N>K):
    #나눠떨어지는 형태로 바꿔주기
    count = count + (N%K)
    N = N - (N%K)

    #나눠주기
    count = count + 1
    N = N//K

#마지막 안나눠지고 남는애들은 1이 되게 만들어주자.(포문에 하면 N이 0이 되어버려 꼬여버림)
count = count + (N-1)
print(count)
